import sys
import math

def solve(dest, hlist):
    tmax = 0.0

    for horse in hlist:
        eta = (float(dest) - float(horse[0]))/ float(horse[1])
        tmax = max(eta, tmax)
        
    return str(float(dest)/tmax)

def parse(f, s):
    l = s.split(" ")
    dest = int(l[0])
    nHorses = int(l[1])
    hlist = []

    for line in xrange(nHorses):
        h = f.readline()
        h = h.split(" ")
        hlist.append((int(h[0]), int(h[1])))

    return solve(dest, hlist)

def process(filenamein):
    f = open(filenamein, "r")
    size = int(f.readline())
    for line in xrange(size):
        s = f.readline()
        res = parse(f, s)
        out = "Case #" + str(line+1) + ": " + res
        print (out)
    f.close()

if len(sys.argv) == 2:
    process(sys.argv[1])