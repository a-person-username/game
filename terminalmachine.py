width = int(input("Level Width: "))
height = int(input("Level Height: "))
grid = []
for i in range(width):
    row = []
    for j in range(height):
        row.append("O")
    grid.append(row)

def search(cell):
    xcoord = []
    ycoord = []
    rownumber = 0
    for row in grid:
        columnnumber = 0
        for square in row:
            if square == cell:
                xcoord.append(columnnumber)
                ycoord.append(rownumber)
            columnnumber += 1
        rownumber += 1
    return xcoord, ycoord

def show():
    for row in grid:
        line = ""
        for square in row:
            line += str(square)
        print(line)

while(True): 
    addition = input("What cell to add? Type TICK for simulation. ") 
    if(len(addition) == 1):
        y = height - int(input("Row? "))
        x = int(input("Column? ")) - 1
        grid[y][x] = addition
    elif(addition == "TICK"):

        coord = search("▷")
        xcoords = coord[0]
        ycoords = coord[1]
        i = 0
        for num in xcoords:
            x = xcoords[i]
            y = ycoords[i]
            grid[y][x] = "O"
            if x == width - 1:
                grid[y][0] = "▷"
            else:
                if grid[y][x + 1] == "⮌": 
                    if x == width - 1:
                        grid[y][width - 1] = "◁"
                    else:
                        grid[y][x - 1] = "◁"
                else: 
                    grid[y][x + 1] = "▷"
            i += 1

        coord = search("◁")
        xcoords = coord[0]
        ycoords = coord[1]
        i = 0
        for num in xcoords:
            x = xcoords[i]
            y = ycoords[i]
            grid[y][x] = "O"
            if x == 0:
                grid[y][width - 1] = "◁"
            else:
                if grid[y][x - 1] == "⮌": 
                    if x == width - 1:
                        grid[y][0] = "▷"
                    else:
                        grid[y][x + 1] = "▷"
                else: 
                    grid[y][x - 1] = "◁"
            i += 1

        coord = search("🢂")
        xcoords = coord[0]
        ycoords = coord[1]
        i = 0
        for num in xcoords:
            x = xcoords[i]
            y = ycoords[i]
            if grid[y][x - 1] != "O":
                grid[y][x + 1] = grid[y][x - 1]

        print(coord)
    else:
        print("ERROR 404")
    show()

# △▷▽◁ ⮌