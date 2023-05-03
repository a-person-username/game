# Asks for level wfidth and height

import numpy as np
width = int(input("Level Width: "))
height = int(input("Level Height: "))

# Creates blank grid 

# grid = np.zeros((width, height))

grid = []
for i in range(width):
    row = []
    for j in range(height):
        row.append(0)
    grid.append(row)

# Creates function that outputs each coordinate of cells matching a cell ID

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

# Creates function to show grid

def show():
    for row in grid:
        line = ""
        for square in row:
            line += str(square)
        print(line)

while(True):

    # Asks for row and column if input is a number

    addition = input("What cell to add? Type TICK for simulation. ")
    if addition != "TICK":
        y = height - int(input("Row? "))
        x = int(input("Column? ")) - 1
        grid[y][x] = int(addition)
    if addition == "TICK":

    # Deletes the original position of 1's and 2's and creates new ones either at the spot next to them or wrapped around the grid

        coord = search(1)
        xcoords = coord[0]
        ycoords = coord[1]
        i = 0
        for num in xcoords:
            x = xcoords[i]
            y = ycoords[i]

            # Sets the original position of the mover to blank
            
            grid[y][x] = 0
            if x == width - 1:
                grid[y][0] = 1
            else:

                # Checks if a flipper is in its path

                if grid[y][x + 1] == 3:
                    if x == width - 1:
                        grid[y][width - 1] = 2
                    else:
                        grid[y][x - 1] = 2

                else:
                    grid[y][x + 1] = 1
            i += 1


        coord = search(2)
        xcoords = coord[0]
        ycoords = coord[1]
        i = 0
        for num in xcoords:
            x = xcoords[i]
            y = ycoords[i]

            # Sets the original position of the mover to blank

            grid[y][x] = 0
            if x == 0:
                grid[y][width - 1] = 2
            else:

                # Checks if a flipper is in its path

                if grid[y][x - 1] == 3:
                    if x == width - 1:
                        grid[y][0] = 1
                    else:
                        grid[y][x + 1] = 1
                else:
                    grid[y][x - 1] = 2
            i += 1

    # There is no code for the flipper (3 ⮌) because the flip is built into left (1 ▷) and right (2 ◁)
    # This does make the code quite asymmetric, but there are always ambiguous situations like ▷ ◁

    show()


# △▷▽◁ 