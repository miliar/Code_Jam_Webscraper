from sys import *
from heapq import *
from time import time
from multiprocessing import Pool
from collections import *
import itertools
from copy import deepcopy
from bisect import *
setrecursionlimit(10000)
from math import *

def readint():
    return int(fi.readline())

def readints():
    return [int(X) for X in fi.readline().split()]

def readstr():
    return fi.readline().rstrip()

def read_case():
    a1 = readint()
    g1 = [readints() for X in range(4)]
    a2 = readint()
    g2 = [readints() for X in range(4)]
    return (a1, g1, a2, g2)

def solve_case(a1, g1, a2, g2):
    p1 = set(g1[a1-1])
    p2 = set(g2[a2-1])
    p = p1 & p2
    if len(p) == 0: return "Volunteer cheated!"
    elif len(p) > 1: return "Bad magician!"
    else: return min(p)

def print_solution(case):
    val = solve_case(*case[1])
    msg = "Case #{}: {}".format(case[0], val)
    print msg
    return msg

t0 = time()
# Initialisation here
t1 = time()
print "Intialisation took %f seconds" % (t1 - t0)
# raw_input("Press enter when the input file has been downloaded: ")

if __name__ == '__main__':
    fni = "%s-%s-%s.in" % (argv[1], argv[2], argv[3])
    fno = "%s-%s-%s.out" % (argv[1], argv[2], argv[3])
    fi = open(fni, 'r')
    fo = open(fno, 'w')
    numcases = readint()
    cases = [(I, read_case()) for I in range(1,1+numcases)]
    mt = False
    if mt:
        print "Running multi-threaded"
        p = Pool(8)
        fo.write('\n'.join(p.map(print_solution, cases)))
    else:
        print "Running single-threaded"
	fo.write('\n'.join(map(print_solution, cases)))
    print "Elapsed time %f seconds " % (time() - t1)

