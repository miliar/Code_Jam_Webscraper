from sys import *
from math import *

def calc_flips(line, size):
    flips = 0
    n = len(line)
    for i in range(0, n-size+1):
        if line[i] == '-':
            flips += 1
            for j in range(size):
                line[i+j] = '+' if line[i+j] == '-' else '-'

    for i in range(size):
        if line[n-i-1] == '-':
            return "IMPOSSIBLE"
    return str(flips)





fin = open(argv[1] + ".in", 'r') 
fout = open(argv[1] + ".out", 'w')
    
ncases = int(fin.readline())
for c in range(0, ncases):
    info = fin.readline().split()
    line = [ p for p in info[0] ]
    size = int(info[1])

    result = calc_flips(line, size)
    fout.write("Case #" + str(c+1) + ": " + result + "\n")

fin.close()
fout.close()

