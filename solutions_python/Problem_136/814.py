#!/usr/bin/python
import sys

def memo(f):
    cache = {}
    def memf(*x):
        if not x in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

def solve(l):
    l = l.split(' ')
    c = float(l[0])
    f = float(l[1])
    X = float(l[2])
    r = 2.0
    x = 0.0

    # while True:
    #     diff = c / r
    #     x1 = x + X / r
    #     x2 = x + diff + X / (r + f)
    #     if x1 < x2:
    #         x = x1
    #         break
    #     else:
    #         r += f
    #         x += diff
    # return x


    cx = 1 - c / X
    r = 2.0
    x = 0
    while True:
        rf = r + f
        lt =  r / rf > cx
        if lt:
            break
        x += c / r
        r = rf
    return x + X / r




#needs an input file
infname = sys.argv[1]
inf = open(infname)
#assumes infname ends with .in
outfname = infname[:-3] + ".out"
#output file can be specified separately
if len(sys.argv) > 2:
    outfname = sys.argv[2]
outf = open(outfname, "w")
case = 1
#ignore 1st line
inf.readline()
while True:
    line = inf.readline()
    if line == '':
        break
    sol = "Case #" + str(case) + ": " + str(solve(line.strip()))
    print sol
    outf.write(sol + "\n")
    case += 1
