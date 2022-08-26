from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header, Body, File, UploadFile, Form, exceptions
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, FastAPI, Body
from fastapi.staticfiles import StaticFiles
from utils.no_accent import no_accent_vietnamese
import shutil
import os
import re
from .convertAudio import convertWav
from .get_song_list import  song_list

router = APIRouter(
    prefix="",
    tags=["audio"],
    # dependencies=[Depends(get_token_header)],
)
# API lấy danh sách tên bài hát


@router.get("/song")
async def song(offset: int = 0, limit: int = 20):
    try:
        # Đọc file để lấy tên bài hát
        songlist = song_list(offset, limit)
        return {
            "code": 200,
            "status": "success",
            "data": songlist
        }
    except Exception as e:
        return {
            "code": 500,
            "status": "error",
            "message": f"Error",
            "description": f'Có một lỗi xảy ra : {e}',
        }

app = FastAPI()

origins = [
    "http://localhost:1611",
    "http://128.199.194.183:1611",
    "https://nlp.aiacademy.edu.vn/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/audios", StaticFiles(directory="corpus_vn"), name="static")


app.include_router(router, prefix="/api")
