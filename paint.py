import keyboard
coltotal = int(input("How many columns would you like? "))
rowtotal = int(input("How many rows would you like? "))
grid = []
for _ in range(rowtotal):
    global row
    row = []
    for _ in range(coltotal):
        row.append("8 ")
    grid.append(row)
for row in grid:
    print(*row)