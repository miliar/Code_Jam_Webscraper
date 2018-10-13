import math
from math import *
 
in_lines = []
in_pos = 0
out_lines = []

'''------------Read data block-----------'''
def readInput():
    global in_lines
    with open('test.in') as f:
        in_lines = f.readlines()

def saveOutput():
    global out_lines
    text_file = open("test.out", "w")
    for s in out_lines:
        text_file.write(s + '\n')
    text_file.close()

def readNextLine():
    global in_pos
    in_pos += 1
    return in_lines[in_pos - 1].replace("\n", "")
'''--------------------------------------'''

'''---------Data analysing block---------'''
grid = []
symbDone = []

def initGrid():
    global grid
    global symbDone
    grid = []
    symbDone = []

def addToGrid(row):
    r = list(row)
    grid.append(r)

	
def recount(r, c):
    global grid
    global symbDone

    symb = grid[r][c]
    if not (symb in symbDone):
        symbDone.append(symb)
        rect = [r, c, r, c]
        
        
            
        canIterate = True
        while canIterate:
            canIterate = False
            if isAvailable([rect[0], rect[1], rect[2] + 1, rect[3] + 1], symb):
                canIterate = True
                rect = [rect[0], rect[1], rect[2] + 1, rect[3] + 1]
                fillRect(rect, symb)
            
            elif isAvailable([rect[0] - 1, rect[1] - 1, rect[2], rect[3]], symb):
                canIterate = True
                rect = [rect[0] - 1, rect[1] - 1, rect[2], rect[3]]
                fillRect(rect, symb)

            elif isAvailable([rect[0] - 1, rect[1], rect[2], rect[3] + 1], symb):
                canIterate = True
                rect = [rect[0] - 1, rect[1], rect[2], rect[3] + 1]
                fillRect(rect, symb)
            
            elif isAvailable([rect[0], rect[1] - 1, rect[2] + 1, rect[3]], symb):
                canIterate = True
                rect = [rect[0], rect[1] - 1, rect[2] + 1, rect[3]]
                fillRect(rect, symb)
            
            elif isAvailable([rect[0] - 1, rect[1], rect[2], rect[3]], symb):
                canIterate = True
                rect = [rect[0] - 1, rect[1], rect[2], rect[3]]
                fillRect(rect, symb)

            elif isAvailable([rect[0], rect[1], rect[2] + 1, rect[3]], symb):
                canIterate = True
                rect = [rect[0], rect[1], rect[2] + 1, rect[3]]
                fillRect(rect, symb)
                            
            elif isAvailable([rect[0], rect[1] - 1, rect[2], rect[3]], symb):
                canIterate = True
                rect = [rect[0], rect[1] - 1, rect[2], rect[3]]
                fillRect(rect, symb)
                            
            elif isAvailable([rect[0], rect[1], rect[2], rect[3] + 1], symb):
                canIterate = True
                rect = [rect[0], rect[1], rect[2], rect[3] + 1]
                fillRect(rect, symb)
		
	
def isCell(r, c):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        return True
    else:
        return False
		
def isAvailable(rect, symb):
    global grid
    available = True
    for i in range(rect[2] - rect[0] + 1):
        for j in range(rect[3] - rect[1] + 1):
            if isCell(rect[0] + i, rect[1] + j):
                if grid[rect[0] + i][rect[1] + j] != "?" and grid[rect[0] + i][rect[1] + j] != symb:
                    available = False
            else:
                available = False	
    return available
	
def fillRect(rect, symb):
    global grid
    for i in range(rect[2] - rect[0] + 1):
        for j in range(rect[3] - rect[1] + 1):
            grid[rect[0] + i][rect[1] + j] = symb
	
def analyseGrid():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "?":
                recount(r, c)
				
	
'''--------------------------------------'''

'''--------------Main block--------------'''
readInput()  # Read the whole input data input
testsCount = int(readNextLine())  # Read the tests count

for n in range(testsCount):
    print n + 1
    splitWords = readNextLine().split()

    rows = int(splitWords[0])
    cols = int(splitWords[1])

    '''Do something with data'''
    initGrid()
    for i in range(rows):
        addToGrid(readNextLine())

    analyseGrid()
    '''----------------------'''
    out_lines.append("Case #" + str(n + 1) + ":")  # Save data result
    for i in range(rows):
        out_lines.append("".join(grid[i]))
    
saveOutput()  # Save the whole output data input
'''--------------------------------------'''
