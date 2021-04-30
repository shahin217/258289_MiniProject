# 9am - 6pm
# Water - audio.mp3 (approx 3.5 litres) - Drank - log - Every 30 min
# Eyes - audio.mp3 - Eyes relaxed - log - Every 45 min
# Relaxation - audio.mp3 every - Relaxed - log - Every 60 min
# Break time - audio.mp3 - Break Done - log - at 2pm
# Break over - audio.mp3 - log - at 3pm
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
        f.close()


def read_log():
    f = open("C:\\Users\\HP\\Desktop\\python\\mylogs.txt", "r+")
    print("Your log file is ")
    print(f.read())
    f.close()


if __name__ == '__main__':

    init_water = time()                     # init_water is the initial time for water.
    init_eyes = time()                      # init_eyes is the initial time for eye relaxation.
    init_relax = time()                     # init_relax is the initial time for body relaxation.
    water_secs = 30 * 60                    # time set for drinking water.
    relax_secs = 60 * 60                    # time set for body relaxation.
    eyes_secs = 45 * 60                     # time set for eye relaxation.

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if time() - init_water > water_secs:
            print("Water Drinking time. Enter 'done' to stop the alarm.")
            music_on_loop('D:\\Music_Dir\\audio.mp3', 'done')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyes_secs:
            print("Eye exercise time. Enter 'done' to stop the alarm.")
            music_on_loop('D:\\Music_Dir\\audio.mp3', 'done')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_relax > relax_secs:
            print("Relaxation Time. Enter 'done' to stop the alarm.")
            music_on_loop('D:\\Music_Dir\\audio.mp3', 'done')
            init_relax = time()
            log_now("Relaxation done at")

        if current_time == "14:00:00":                                  # Break time
            print("Break Time. Enter 'done' to stop the alarm.")
            music_on_loop('D:\\Music_Dir\\audio.mp3', 'done')
            log_now("Break at")

        if current_time == "15:00:00":                                  # Break over
            print("Break Over. Enter 'done' to stop the alarm.")
            music_on_loop('D:\\Music_Dir\\audio.mp3', 'done')
            log_now("Break over at")

        if current_time == "18:00:00":                                  # Time over
            print("Time over. Enter 'done' to stop the alarm.")
            music_on_loop('D:\\Music_Dir\\audio.mp3', 'done')
            log_now("Time over at")
            break

    print("You have successfully followed your schedule.\nThank you!")
    print("Do you want to read the log file: y/n")
    ch = input()
    if ch == 'y':
        read_log()
    else:
        print("Have a nice day!")
