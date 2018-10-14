#!/usr/bin/env python

def getMaximumValues(lawn):
    rowMax = []
    colMax = []
    for x in range(row):
        rowMax.append(0)
        for y in range(col):
            if lawn[x][y] > rowMax[-1]:
                rowMax[-1] = lawn[x][y]
    for x in range(col):
        colMax.append(0)
        for y in range(row):
            if lawn[y][x] > colMax[-1]:
                colMax[-1] = lawn[y][x]
    return rowMax, colMax

def checkValidLawn(rowMax, colMax, lawn):
    for rows, rowM in zip(lawn, rowMax):
        for patch, colM  in zip(rows, colMax):
            if patch < rowM and patch < colM:
                return "NO"
    return "YES"

if __name__ == "__main__":

    #input_file="B-small-attempt0.in"
    input_file="B-Large.in"
    fin = open(input_file)
    
    #fout=open('lawnMower.txt','w')
    fout=open('lawnMowerLarge.txt','w')

    testCases = int(fin.readline().rstrip()) 

    for i in range(1, testCases+1):
    	case = "Case #%d: " %(i)
        fout.write(case)
        lawn = []
        line = fin.readline().rstrip().split()
        row = int(line[0])
        col = int(line[1])
        for x in range(row):
        	lawn.append([int(i) for i in fin.readline().rstrip().split()])
        rowMax, colMax = getMaximumValues(lawn)
        fout.write(checkValidLawn(rowMax, colMax, lawn) + "\n")
    
    fout.close()
    fin.close()

