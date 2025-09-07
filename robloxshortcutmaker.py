from win32com.client import Dispatch

import requests,json,urllib.request,PIL.Image,os

from tkinter import *

saveplace = os.path.join(r"C:\Users",os.environ.get("USERNAME"))
desktop = os.path.join(saveplace,"Desktop")

def CreateShortcut(gameplaceid,name):

    global report
    
    pngplace = os.path.join(saveplace,f"shortcutmakerimage{gameplaceid}.png")
    icoplace = os.path.join(saveplace,f"shortcutmakerimage{gameplaceid}.ico")

    path = os.path.join(desktop,name+".lnk")
    target = "roblox://placeId="+str(gameplaceid)+"/"
    work_dir = desktop

    universedata = requests.get(f"https://apis.roblox.com/universes/v1/places/{gameplaceid}/universe")

    universeid = json.loads(universedata.content)["universeId"]

    if universeid == None:
        report.configure(text="Can't create. This game ID Doesn't exist.")
        return False
    
    gameicon = json.loads(requests.get(f"https://thumbnails.roblox.com/v1/games/icons?universeIds={universeid}&returnPolicy=PlaceHolder&size=50x50&format=Png&isCircular=false").content)
    imagedata = gameicon["data"][0]["imageUrl"]

    urllib.request.urlretrieve(imagedata,pngplace)

    image = PIL.Image.open(pngplace)

    try:
        print('removed')
        os.remove(icoplace)
    except:
        print("already gone")
        pass

    image.save(icoplace,format="ICO")

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = work_dir
    shortcut.IconLocation = icoplace+",0"
    shortcut.save()

    report.configure(text="Created! Check your desktop.")

    os.remove(pngplace)

    return True

window = Tk()
window.title("Game Shortcut Creator")

# Adjust size 
window.geometry("500x200")

# Specify Grid
Grid.rowconfigure(window,0,weight=1)
Grid.columnconfigure(window,0,weight=1)

Grid.rowconfigure(window,1,weight=1)

# Create Buttons
report = Label(window,text="Type a game ID on the upper box and shortcut name on the lower one.")
gameid = Entry(window)
button = Button(window,text="Create Shortcut")
gamename = Entry(window)

# Set grid
report.grid(row=0,column=0,sticky="NSEW")
gameid.grid(row=1,column=0,sticky="NSEW")
gamename.grid(row=2,column=0,sticky="NSEW")
button.grid(row=3,column=0,sticky="NSEW")

button.configure(command=lambda:CreateShortcut(gameid.get(),gamename.get()))

# Execute tkinter
window.mainloop()

mainloop()