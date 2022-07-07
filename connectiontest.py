from tkinter import *
import speedtest

root = Tk()
root.title("Connection speed test")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg="#1a212d")


def check():
    test = speedtest.Speedtest()
    uploading = round(test.upload()/(1024*1024), 2)
    upload.config(text=uploading)
    downloading = round(test.download()/(1024*1024), 2)
    download.config(text=downloading)
    Download.config(text=downloading)
    servernames = []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# images
Top = PhotoImage(file="top.png")
Label(root, image=Top, bg="#1a212d").pack()

Main = PhotoImage(file="main.png")
Label(root, image=Main, bg="#1a212d").pack(pady=(40, 0))

start_button = PhotoImage(file="button.png")
Button = Button(root, image=start_button, bg="#1a212d", activebackground="#1a212d", bd=0, cursor="hand2", command=check)
Button.pack(pady=10)

# labels
Label(root, text="Ping", font="consolas 10 bold", bg="#384056").place(x=55, y=0)
Label(root, text="Download", font="consolas 10 bold", bg="#384056").place(x=150, y=0)
Label(root, text="Upload", font="consolas 10 bold", bg="#384056").place(x=265, y=0)

Label(root, text="ms", font="consolas 7 bold", bg="#384056", fg="white").place(x=60, y=80)
Label(root, text="Mb/s", font="consolas 7 bold", bg="#384056", fg="white").place(x=165, y=80)
Label(root, text="Mb/s", font="consolas 7 bold", bg="#384056", fg="white").place(x=275, y=80)

Label(root, text="Download", font="consolas 15 bold", bg="#384056", fg="white").place(x=140, y=280)
Label(root, text="Mb/s", font="consolas 15 bold", bg="#384056", fg="white").place(x=155, y=380)

ping = Label(root, text="00", font="consolas 13 bold", bg="#384056", fg="white")
ping.place(x=70, y=60, anchor="center")

download = Label(root, text="00", font="consolas 13 bold", bg="#384056", fg="white")
download.place(x=180, y=60, anchor="center")

upload = Label(root, text="00", font="consolas 13 bold", bg="#384056", fg="white")
upload.place(x=290, y=60, anchor="center")

Download = Label(root, text="00", font="consolas 40 bold", bg="#384056")
Download.place(x=185, y=350, anchor="center")


root.mainloop()
