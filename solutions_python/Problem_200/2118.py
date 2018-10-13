import sys, string
import time
import random
import math

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def tidy(N):
    z = 1
    while str(N) != "".join(sorted(str(N))):
        N -= z * ((N/z) % 10 + 1)
        z *= 10
        #~ print(N)
    return N

T = readint()
for t in range(T):
    N = readint()

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    print tidy(N)
