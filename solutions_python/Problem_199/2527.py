#-------------------------------------------------------------------------------
# Name:        Oversized Pancake Flipper
# Purpose:
#
# Author:      poorb
#
# Created:     08/04/2017
# Copyright:   (c) poorb 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def check(arr):

    for ch in arr:
        if ch == "-":
            return False

    return True
def resolve(tup):
    data = [ch for ch in  tup[0]]
    number = tup[1]
    numofoperation=0
    maxstart = len(data) -number
    start = 0
    while not check(data):
        #print("{0}:{1}".format(numofoperation, "".join(data)))
        idx = -1
        for i in range(start, len(data) +  number - 1):
            if data[i] == "-":
                idx = i
                break
        if idx == -1:
            break
        start = idx
        if start > maxstart :
            return "IMPOSSIBLE"

        for i in range(start, start + number ):
            if data[i] == "+":
                data[i] = "-"
            else:
                data[i] = "+"
        start = start+1
        numofoperation +=1

    return numofoperation
def dataParser(string):
    a,b = string.split()
    return a, int(b)
def test1():
    line = "---+-++- 3"
    print("line=[{0}] result={1}".format( line, resolve(dataParser(line))))
def test2():
    line = "+++++ 4"
    print("line=[{0}] result={1}".format( line, resolve(dataParser(line))) )
def test3():
    line = "-+-+- 4"
    print("line=[{0}] result={1}".format( line, resolve(dataParser(line))))
def readandresolve(read):
    n = int(read().strip())
    data = [resolve(dataParser(read().strip())) for i in range(n)]
    return data
def main():

    #r = sys.stdin.readline
    with open("A-large.in","r") as infile:
        r = infile.readline
        data = readandresolve(r)

    with open("OversizedPancakeFlipperOut.txt","w") as outfile:
         for idx,result in enumerate( data):
            outfile.write("Case #{0}: {1}\n".format(idx+1, result))

if __name__ == '__main__':
    main()
