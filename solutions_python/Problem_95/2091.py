#from __future__ import division
import sys, string
import itertools
from math import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

f = open("A-map.in", "r")
A = f.readline()
B = f.readline()

M = {}
for i in range(len(A)):
    M[A[i]] = B[i]

T = int(sys.stdin.readline())

for k in range(T):
    coded = sys.stdin.readline().strip("\n")
    decoded = ""
    for c in coded:
        decoded += M.get(c, "*")
        
    print >> sys.stderr, k
    print "Case #%d: %s" % (k+1, decoded)
