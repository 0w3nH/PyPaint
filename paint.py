import keyboard
import time
import os

colTotal = int(input("How many columns would you like? "))
rowTotal = int(input("How many rows would you like? "))
cursorRow = 0
cursorCol = 0
flashCursor = True
timeSinceFlash= time.time()
extraTime = 0
grid = []
for _ in range(rowTotal):
    global row
    row = []
    for _ in range(colTotal):
        row.append("8 ")
    grid.append(row)
for row in grid:
    print(*row)
while True:
    global cursorLockCol
    global cursorLockRow
    currentTime = time.time()+extraTime
    if currentTime - timeSinceFlash > 0.5: 
        if flashCursor == True:
            cursorLockRow = cursorRow
            cursorLockCol = cursorCol
            charlock = grid[cursorRow][cursorCol]
            grid[cursorRow][cursorCol] = "  "
            flashCursor = False
        elif flashCursor == False:
            grid[cursorLockRow][cursorLockCol] = charlock
            flashCursor = True
        timeSinceFlash = currentTime
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        for row in grid:
            print(*row)

    if keyboard.is_pressed("left arrow") or keyboard.is_pressed("a"):
        cursorCol = cursorCol - 1
        if cursorCol == -1:
            cursorCol = colTotal - 1
        
        grid[cursorLockRow][cursorLockCol] = charlock
        flashCursor = True
        extraTime = extraTime + 1
        time.sleep(0.3)
    if keyboard.is_pressed("right arrow") or keyboard.is_pressed("d"):
        cursorCol = cursorCol + 1
        if cursorCol == colTotal:
            cursorCol = 0
        
        grid[cursorLockRow][cursorLockCol] = charlock
        flashCursor = True
        extraTime = extraTime + 1
        time.sleep(0.3)
    if keyboard.is_pressed("up arrow") or keyboard.is_pressed("w"):
        cursorRow = cursorRow - 1
        if cursorRow == -1:
            cursorRow = rowTotal - 1
        
        grid[cursorLockRow][cursorLockCol] = charlock
        flashCursor = True
        extraTime = extraTime + 1
        time.sleep(0.3)
    if keyboard.is_pressed("down arrow") or keyboard.is_pressed("s"):
        cursorRow = cursorRow + 1
        if cursorRow == rowTotal:
            cursorRow = 0
        
        grid[cursorLockRow][cursorLockCol] = charlock
        flashCursor = True
        extraTime = extraTime + 1
        time.sleep(0.3)
    if keyboard.is_pressed("p"):
        time.sleep(0.5)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        setCharTo = input("\rCustom Character: ")
        time.sleep(0.3)
        if len(setCharTo) == 1:
            grid[cursorRow][cursorCol] = setCharTo+" "
        elif len(setCharTo) == 0:
            grid[cursorRow][cursorCol] = "  "
        else:
            grid[cursorRow][cursorCol] = setCharTo[len(setCharTo)-1]+" "
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        charlock = grid[cursorRow][cursorCol]

    time.sleep(0.001)





    # I might fix this later
'''
for charnum in range(31, 64):
        if keyboard.is_pressed(chr(charnum)):
            grid[cursorRow][cursorCol] == chr(charnum), " "
    for charnum in range(90, 95):
        if keyboard.is_pressed(chr(charnum)):
            grid[cursorRow][cursorCol] == chr(charnum), " " 
    for charnum in range(122, 125):
        if keyboard.is_pressed(chr(charnum)):
            grid[cursorRow][cursorCol] == chr(charnum), " "
    if keyboard.is_pressed("delete"):
        grid[cursorRow][cursorCol] == "  " 
'''