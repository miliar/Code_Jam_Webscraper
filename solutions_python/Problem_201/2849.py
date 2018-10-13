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
    return do_run(N, [], K)

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

if __name__ == '__main__':
    loops = int(stdin.readline())
    for i in range(0,loops):
        Data = stdin.readline()
        print "Case #%d: %s" % (i+1, str(run(Data)))
