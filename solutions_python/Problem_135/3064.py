#!/usr/bin/python
import sys

def makeTable(lines): #makes a 4x4, but list of lists
    ret = []
    for l in lines:
        l = l.strip();
        row = map(int, l.split(" "))
        ret.append(row)
    return ret

def solve(inp):
    vA = int(inp[0]) - 1
    tA = makeTable(inp[1:5]) #has to parse as ints
    vB = int(inp[5]) - 1
    tB = makeTable(inp[6:11])
    ans = set(tA[vA]) & set(tB[vB])
    if (len(ans) == 0):
        return "Volunteer cheated!"
    elif (len(ans) == 1):
        return str(ans.pop())
    else:
        return "Bad magician!"

if len(sys.argv) != 3:
    print "Usage: "+ sys.argv[0]  +" infile outfile"
    exit(1)
infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
lines = infile.readlines() 
N = int(lines[0])
lAcc = 1;
for n in range(1, N+1):
    lineNo = (n-1)*10+1
    outfile.write("Case #"+str(n)+": " + solve(lines[lineNo:lineNo+10])+"\n")
