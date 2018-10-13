#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     14-04-2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys;
import fileinput;
import array;

LINES_PER_QUESTION=5
top=0

def checkLine(line,height):
    for h in line:
        if int(h) > height:
            return False
    return True

def checkVert(lawn,r,c):
    height = int(lawn[r][c])
    cols = [r[c] for r in lawn]

    return checkLine(cols,height)

def checkHori(lawn,r,c):
    height = int(lawn[r][c])
    rows = lawn[r]

    return checkLine(rows,height)

def check(lawn,r,c):
    return checkVert(lawn,r,c) or checkHori(lawn,r,c)

def solve(data):
    global top

    dimension = data[0].split(' ')

    rows=int(dimension[0])
    cols=int(dimension[1])

    top=top+1+rows
    data=data[1:rows+1]

    if rows==1 or cols==1: return 'YES'
    lawn = [datum.strip().split(' ') for datum in data]

    for r in range(rows):
        for c in range(cols):
            if not check(lawn,r,c): return 'NO'

    return 'YES'

def main():
    global top

    data = [line for line in fileinput.input('B-large.in')]
    qcount = int(data[0])

    data = data[1:]

    for i in range(qcount):
        result = solve(data[top:])
        print("Case #%d: %s"%(i+1,result))

if __name__ == '__main__':
    main()