import uvicorn
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="localhost", port=1610, reload=True) # 128.199.194.183