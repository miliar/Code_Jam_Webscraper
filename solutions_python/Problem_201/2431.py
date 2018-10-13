#!/usr/bin/python
import sys
import unittest
import math
from sys import stdin
Debug=False

def d(Str):
    if Debug: print Str

def run(data):
    d("new test %s" %data)
    [N,K] = data.split(' ')
    N = int(N)
    K = int(K)
    #return do_calc(N,K)
    return do_run(N, [], K)

def do_calc(N,K):
    level = int(math.log(K,2))+1
    lost = int(math.pow(2,level) - 1)
    left = int(N - lost)
    #base = int(math.pow(2, int(math.log(N,2)) - level))
    base = int(N / math.pow(2, level -1))
    lowbound = math.pow(2,level-1)
    highbound = math.pow(2,level)
    if base == 1:
        special = left
    else:
        special = left % (base-1)

    slots = math.pow(2, level)
    groups = slots / 2
    d("level: %d, left: %d, base: %d, special: %d,lowbound: %d, groups: %d" % (level, left,base,special,lowbound,groups))

    if left < 0:
        return "0 0"
    elif base == 0:
        return "%d %d" % (0, 0)
    elif special == 0:
        return "%d %d" % (base, base-1)
    elif special > groups and special / 2 > K - lowbound:
        return "%d %d" % (base, base)
    elif special > groups:
        return "%d %d" % (base, base-1)
    elif special > K - lowbound:
        return "%d %d" % (base, base-1)
    else:
        return "%d %d" % (base-1, base-1)

def do_run(N, C, K):
#    if N == K:
#        return "0 0"
    if N == 1:
        return "0 0"
    if N % 2  == 1:
        Ls = N/2
        Rs = Ls
    else:
        Rs = N/2
        Ls = Rs - 1
    d("run with N: %d Left:%d, Canidates:%s\n Ls: %d Rs: %d" % (N,K,C, Ls, Rs))
#    if (Ls < 0 or  Rs < 0):
#        return "0 0"
    if K == 1:
        return "%d %d" % (max(Ls, Rs), min(Ls,Rs))
    else:
        C.append(Ls)
        C.append(Rs)
        C.sort()
        return do_run(C[-1], C[-K:-1], K -1)

class TestMe(unittest.TestCase):
    def test_example(self):
        self.assertEqual("1 0", run("4 2"))
        self.assertEqual("1 0", run("5 2"))
        self.assertEqual("1 1", run("6 2"))
        self.assertEqual("0 0", run("1000 1000"))
        self.assertEqual("500 499", run("1000 1"))
        self.assertEqual("0 0", run("3 2"))
        self.assertEqual("3 3", run("500 114"))
        ## prepare for small2 and large
        self.assertEqual("64 64", run("129 1"))
        self.assertEqual("32 31", run("129 2"))
        self.assertEqual("32 31", run("129 3"))
        self.assertEqual("16 15", run("129 4"))
        self.assertEqual("16 15", run("129 5"))
        self.assertEqual("15 15", run("129 6"))
        self.assertEqual("15 15", run("129 7"))
        self.assertEqual("8 7", run("129 8"))
        self.assertEqual("8 7", run("129 9"))
        self.assertEqual("7 7", run("129 10"))
        self.assertEqual("7 7", run("129 11"))
        self.assertEqual("7 7", run("129 12"))
        self.assertEqual("7 7", run("129 13"))
        self.assertEqual("7 7", run("129 14"))
        self.assertEqual("7 7", run("129 15"))
        self.assertEqual("4 3", run("129 16"))
        self.assertEqual("4 3", run("129 17"))
        self.assertEqual("3 3", run("129 18"))
        self.assertEqual("3 3", run("129 19"))
        self.assertEqual("3 3", run("129 21"))
        self.assertEqual("3 3", run("129 22"))
        self.assertEqual("3 3", run("129 23"))
        self.assertEqual("3 3", run("129 24"))
        self.assertEqual("3 3", run("129 25"))
        self.assertEqual("3 3", run("129 26"))
        self.assertEqual("3 3", run("129 27"))
        self.assertEqual("3 3", run("129 28"))
        self.assertEqual("3 3", run("129 29"))
        self.assertEqual("3 3", run("129 30"))
        self.assertEqual("3 3", run("129 31"))
        self.assertEqual("2 1", run("129 32"))

if __name__ == '__main__':
    loops = int(stdin.readline())
    for i in range(0,loops):
        Data = stdin.readline()
        print "Case #%d: %s" % (i+1, str(run(Data)))
