#!/usr/bin/python3
# compare.py
import argparse
import os
import glob

def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument("-limit ", "--limit", help="limit")
    parser.add_argument("-offset ", "--offset", help="offset")
    args = parser.parse_args()

    offset = args.offset if args.offset else 0
    limit = args.limit if args.limit else 20
    return offset, limit


def song_list(offset, limit):
    index = 0
    path = os.path.join(os.getcwd(), 'corpus_vn')
    songlist = []
    # os.chdir(path)
    for l in glob.glob(path+'/*'):
        print(l)
        if not os.path.exists(f'{l}/text.txt') or len(os.listdir(l)) == 1:
            pass
        elif index >= offset and index < offset+limit:
            # print(f'Index: {index} - {l}')
            # os.system(f'sed -n 1p {l}/text.txt')
            text = os.popen(f'sed -n 1p {l}/text.txt').read()
            audio = l + '/'+text.split('|')[0] + '.wav'
            # print(audio)
            songlist.append({
                'song_id': os.path.basename(l),
                'lyric': text,
                'audio': audio
            })

        index += 1
    return songlist


if __name__ == "__main__":
    offset, limit = initialize()
    song_list(offset, limit)
