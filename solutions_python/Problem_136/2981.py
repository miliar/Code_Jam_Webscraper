#!/usr/bin/python
import sys

def solve(line):
    C = F = X = B = 0
    [C, F, X] = map(float, line.split(" "))
    B = 2.0
    T = float("inf")
    n = 0;
    tNplus1 = X/B
    fAcc = 0
    while (tNplus1 < T):
        T = tNplus1
        n += 1
        fAcc += C / (B + (n-1)*F)
        tNplus1 = X / (B + n*F) + fAcc
    return str(T)

if len(sys.argv) != 3:
    print "Usage: "+ sys.argv[0]  +" infile outfile"
    exit(1)
infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
lines = infile.readlines() 
N = int(lines[0])
for n in range(1, N+1):
    outfile.write("Case #"+str(n)+": " + solve(lines[n].strip())+"\n")
