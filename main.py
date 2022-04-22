import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog,messagebox

def createWidgets():
    link_label = Label(root, text="Youtube URL: ", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination: ", bg="#E8D579")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=downloads_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Browse", command=browse, width=10, bg="#05E8E0")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Download Video", command=download_video, width=10, bg="#05E8E0")
    download_but.grid(row=3, column=1, pady=3, padx=3)


def browse():

    download_dir = filedialog.askdirectory(initialdir="Your directory path")

    downloads_path.set(download_dir)


def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    downloads_path.set(download_Directory)


# Defining Download() to download the video

def download_video():

    url = video_link.get()
    folder=downloads_path.get()

    get_video=YouTube(url)
    get_stream=get_video.streams.first()
    get_stream.download(folder)

    messagebox.showinfo("Success"+folder)

root=tk.Tk()

root.geometry("600x120")
root.resizable(False,False)
root.title("Pytubbe")
root.config(background="#000000")

video_link = StringVar()
downloads_path = StringVar()

createWidgets()

root.mainloop()
