#! /usr/bin/python

import sys



def whoWins(x,r,c):
    nSquares = r*c
    if nSquares%x != 0:
        return "RICHARD"
    if x == 2:
        return "GABRIEL"
    if x/2+1 > min(r,c):
        return "RICHARD"
    if x == 3:
        return "GABRIEL"
    return "GABRIEL"

def getData(fileName):
    f = open(fileName,'r+')
    lines = [line for line in f]
    lines = map(lambda x:x.replace("\n",""),lines)
    nCases = int(lines[0])
    k = 1
    while k <= nCases:
        intValues = map(int,lines[k].split(" "))
        x,r,c = intValues[0], intValues[1], intValues[2]
        print "Case #"+str(k)+": "+whoWins(x,r,c)
        k = k+1


if __name__ == "__main__":
    fileName = sys.argv[1]
    getData(fileName)

