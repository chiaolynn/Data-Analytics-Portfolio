
"""
Created on Fri Oct  7 20:32:15 2022

@author: lynn Chiao
"""
from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar.

format = input("Convert to MP4 or MP3? ")


def question():
    format = input("MP4 or MP3? ")
    if format == "MP4" or format == "mp4":   
        converttomp4()
    elif format == "MP3" or format == "mp3":
        converttomp3()

def converttomp4():
    num = int(input("for how many videos? "))
    i=0
    while i < num:       
        video_url = input("Copy the youtube video link here: ")
        yt=YouTube(video_url,on_progress_callback=on_progress)
        print("You're now downloading...':", yt.title)
        videos=yt.streams.get_highest_resolution()
        #videos.download(save_path)
        videos.download()
        print("\nDone! Enjoy!! :)")
        i+=1

def converttomp3():
    num = int(input("for how many videos? "))
    i=0
    while i < num: 
        video_url = input("Copy the youtube video link here: ")
        yt = YouTube(video_url,on_progress_callback=on_progress)
        print("You're now downloading...':", yt.title)
        videos=yt.streams.filter().get_audio_only()
        videos.download(filename=yt.title+'.mp3')
        print("\nDone! Enjoy!! :)")
        i+=1
 
if format == "MP4" or format == "mp4":   
    converttomp4() #一定要「先定義函式，再執行函式」
elif format == "MP3" or format == "mp3":
    converttomp3()
    
prompt = input("would you like to run program again?(y/n): ")

if prompt == "y" or prompt =="yes":
    question()
else:
    input("BYE! See ya!!")

input()
