from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

import pytube
from pytube import YouTube

Folder_Name = " "
#select

#FileLocation
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locError.config(text = Folder_Name, fg = "green")

    else:
        locError.config(text = "Please choose an directory!!", fg = "red")


#download video
def downloadVideo():
    choice = ytdchoice.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text = "")
        yt = pytube.YouTube(url)
        video = yt.streams.first()
        video.download(Folder_Name)
        #d_video.download(Folder_Name)

        # if(choice == choice[0]):
        #     selected = yt.streams.filter(progressive = True).first()

        # #elif(choice == choice[1]):
        #     #selected = yt.streams.filter(progressive = True, file_extension = 'mp4').second()

        # elif(choice == choice[1]):
        #     selected = yt.streams.filter(progressive = True, file_extension = 'mp4').last()

        # elif(choice == choice[2]):
        #     selected = yt.streams.filter(only_audio = True).first()

        # else:
        #     ytdError.config(text = "Paste Link again", fg = "red")

    #download function
    # selected.download(Folder_Name)
    #select.download()
    ytdError.config(text= "Download Completed!!")



ytube = Tk()
ytube.title("YouTube downloader")
ytube.geometry("600x700")   #set window
ytube.columnconfigure(0,weight=1)    #set all contents in center

#ytd link label
ytdLabel = Label(ytube, text = "Enter the url of the video: ",font = ("jost",24))
ytdLabel.grid()

#entry box
ytdEntryVar = StringVar()
ytdEntry = Entry(ytube, width = 50, textvariable = ytdEntryVar)
ytdEntry.grid()

#errorMsg
ytdError = Label(ytube, text = "Error msg", fg = "red", font = ("jost", 15))
ytdError.grid()

#saveLabel
saveVideo = Label(ytube, text = "save the videos", fg = "green", font = ("jost", 15, "bold"))
saveVideo.grid()

#btn to save file
SaveBtn = Button(ytube, width = 10, bg = "red", fg = "white", text = "Choose Path", command=openLocation)
SaveBtn.grid()

#Error msg location
locError = Label(ytube, text = "Error msg of path", fg = "red", font = ("jost", 15))
locError.grid()

#download quality
ytdQuality = Label(ytube, text = "Choose Quality", font = ("jost", 15))
ytdQuality.grid()

#combobox
choice = ["720p", "360p", "Only audio"]
ytdchoice = ttk.Combobox(ytube, values = choice)
ytdchoice.grid()

#download btn
downloadBtn = Button(ytube, text = "Download", bg = "red", fg = "white", width = 10, command= downloadVideo)
downloadBtn.grid()

#developerLabel
developer = Label(ytube, text = "Tapati", font = ("jost", 10))
developer.grid()


ytube.mainloop()


#python -m pip install --upgrade pytube