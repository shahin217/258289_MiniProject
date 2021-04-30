# 258289_MiniProject

## INTRODUCTION
Assume that a programmer works at the office from 9am-6pm. We have to take care of his health and remind him the following things:
*	To drink approx. of 3.5litre water after some time interval between 9-6pm.
*	To do eye exercise after every 45 minutes.
*	To relax the body after every 60 minutes (like move head round and round, left and right for at least one min).
*	To have a break for one hour at 2pm.
*	To come back at 3pm.
*	Over time at 6pm.

The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he is notified to do some activity.
User should enter “done” to stop the audio.

After the user enters the input, a file (log file) should be created for every task, which contains the details about the time when the user performed a certain activity.

## INSTRUCTIONS
In order to run this, you need to:
*	Download the audio.
*	Either change the path of downloaded audio file in your system according to project or change the path in the project according to the downloaded audio file.
*	Set the “Windows Media Player” as default for playing the audio.
*	Change the timings (water_secs) to check the output instantly. (For example, water drinking time is after every 30min, you can change it to 1min or seconds and similarly the others).
*	Log file (mylogs.txt file) will be generated where there is all other PyCharm files are stored. In order to read that file, we need to change the path in the function named as “read_log” in the project. 
*	Log file should be visible only when program will come out of loop at specified time (i.e., at 6pm) through program, else you can check it manually.
