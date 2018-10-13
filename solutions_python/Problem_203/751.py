import sys
from collections import defaultdict
from sortedcontainers import SortedList


def main():
    inputFile = open(sys.argv[1],"r")
    numCases = int(inputFile.readline())
    for t in range(1,numCases+1):
        r, c = inputFile.readline().strip().split(" ")
        r, c = int(r), int(c)
        grids = []
        initials = []
        for i in range(r):
            grids.append([])
            line = inputFile.readline().strip()
            for j in range(c):
                grids[i].append(line[j])
                if (line[j]!="?"):
                    initials.append((i,j,line[j]))
        initials.sort(cmp=initialsComp)
        for initial in initials:
            row, column, letter = initial
            columnLeft = column
            while (columnLeft>0 and grids[row][columnLeft-1]=="?"):
                columnLeft =  columnLeft - 1
            columnRight = column
            while (columnRight<c-1 and grids[row][columnRight+1]=="?"):
                columnRight = columnRight + 1
            rowTop = row
            while (rowTop>0 and not occupied(columnLeft,columnRight,rowTop-1,grids)):
                rowTop = rowTop - 1
            rowBottom = row
            while (rowBottom<r-1 and not occupied(columnLeft,columnRight,rowBottom+1,grids)):
                rowBottom = rowBottom + 1
            for i in range(rowTop,rowBottom+1):
                for j in range(columnLeft,columnRight+1):
                    grids[i][j] = letter
        print("Case #%i:"%(t))
        for i in range(r):
            s = ""
            for j in range(c):
                s += grids[i][j]
            print s
        

def occupied(columnLeft,columnRight,row,grids):
    for i in range(columnLeft,columnRight+1):
        if grids[row][i] != "?":
            return True
    return False

def initialsComp(initialA,initialB):
    r1, c1, letter1 = initialA
    r2, c2, letter2 = initialB
    if (r1+c1)<(r2+c2):
        return -1
    if (r1+c1)>(r2+c2):
        return 1
    if (r1<r2):
        return -1
    if (r1>r2):
        return 1
    if (c1<c2):
        return -1
    else:
        return 1

        
main()