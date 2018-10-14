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

def readfloats():
    return [float(X) for X in fi.readline().split()]

def readstr():
    return fi.readline().rstrip()

def read_case():
    n = readint()
    mn = readfloats()
    mk = readfloats()
    return (n, mn, mk)

def solve_case(n, mn, mk):
    mn.sort()
    mk.sort()
    cn = [sum(1 if K < N else 0 for K in mk) for N in mn]
    cn.reverse()
    z = 0
    for N in mn:
        if max(mk) > N:
            mk.remove(min(K for K in mk if K > N))
        else:
            z += 1
            mk.remove(min(mk))
    y = min(a+b for (a,b) in zip(range(len(cn)), cn))
    return (y, z)
    
def print_solution(case):
    val = solve_case(*case[1])
    msg = "Case #{}: {} {}".format(case[0], *val)
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

