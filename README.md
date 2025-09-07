# Roblox-game-shortcut-creator
(This tool is unofficial and not affiliated with Roblox.)
A Roblox tool meant for creating shortcuts to enter games right from the desktop
This tool uses the Roblox launch protocol (roblox://placeId=1234567890/) trick in order to create shortcuts

## How to build (for Windows)
1. Download the `source.py` file from this repo
2. Download and Install the latest version of python from https://www.python.org/
3. Open Command Prompt and type `pip install pyinstaller` and let it finish installation.
4. Make a folder anywhere you want, and put the source.py file inside of there. (DONT RENAME `source.py`)
5. Make a file in the same folder called `buildexe.txt` and open it and write `pyinstaller --onefile --noconsole source.py`
6. Rename `buildexe.txt` to `buildexe.bat` and double click to run. Once pyinstaller finishes doing what it's doing, you can delete `buildexe.bat`
7. Open the newly created folder called `dist` and inside should be `source.exe`
8. Congratulations! You can now delete the folder you created for `source.py` at the start and just take out the `source.exe` which you are allowed to rename and use.
