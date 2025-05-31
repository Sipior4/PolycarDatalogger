import time

FPS = 60

while True:
    print(f"\rCurrent time: {time.strftime('%Y-%m-%d %H:%M:%S')}", end="")
    time.sleep(1 / FPS)