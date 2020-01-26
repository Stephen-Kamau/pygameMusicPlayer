import os
import pygame
from tkinter import*
from tkinter.filedialog import askdirectory


root=Tk()

root.minsize(600,600)
#stores the songs in a list
songstorelist=[]
#define an index to hold the first song in the list
index=0

songs=StringVar
songlabel=Label(root,textvariable=songs)

def playsong():
	for x in songstorelist:
		pygame.mixer.music.load(x)
		pygame.mixer.music.play()

def nextsong():
    global index
    index = index + 1
    pygame.mixer.music.load(songstorelist[index])
    pygame.mixer.music.play()


def previoussong():
     global index
     index =index - 1
     pygame.mixer.music.load(songstorelist[index])
     pygame.mixer.music.play()



def stopsong():
    pygame.mixer.music.stop()


def selectsongdirectory():
    directory=askdirectory()
    os.chdir(directory)#change working directory into the dir that user selects
    for files in os.listdir(directory):
    	#extensions to be used to select musics
        if files.endswith(".mp3") :
            songstorelist.append(files)
            print (files)

    pygame.mixer.init()
    pygame.mixer.music.load(songstorelist[0])
    pygame.mixer.music.play()



#creating my GUI
    C = Canvas(root, bg="blue", height=250, width=300) 
    coord = 10, 50, 240, 210 
    arc = C.create_arc(coord, start=0, extent=150, fill="red") 
    C.pack() 
    label=Label(root,text="Music Player Using Tkinter")
    label.pack()

    listbox=Listbox(root)
    listbox.pack()
    songstorelist.reverse()
    #show musics selected in the window
    for items in songstorelist:
        listbox.insert(0,items)
    songstorelist.reverse()

    playbuttton=Button(root,text="play",fg="pink",command=playsong)
    nextbutton=Button(root,text="next",command=nextsong,fg="green")
    previousbutton=Button(root,text="previous",command=previoussong,fg="red")
    pausebutton=Button(root,text="pause",command=stopsong)
    stopbutton=Button(root,text="stop",command=stopsong,fg="orange")

    playbuttton.pack()
    nextbutton.pack()
    previousbutton.pack()
    stopbutton.pack()

selectsongdirectory()
songlabel.pack()
root.mainloop()
