import sys # standard Python library
import itertools # standard Python library
#from PerfectAllocation import PerfectAllocation # http://pastebin.com/5sv1quf0
from operator import itemgetter # standard Python library
import bisect # standard Python library
import math # standard Python library
import copy # standard Python library
from fractions import gcd # standard Python library
from utilities import *  # this is helper file which can be found at http://pastebin.com/5gkyim8x
#from blist import blist # add-on library which can be downloaded from https://pypi.python.org/pypi/blist/
from collections import deque


sys.setrecursionlimit(1000) #1000 is default
Prep = []


def preprocess():
    return None
    
def readinput(Input):
    n = Input.readint()
    N = Input.readints()
    
    assert (len(N) == n)
    
    return N


def brute(N):
    def test(N):
        i = 0;
        while i < len(N) - 1 and N[i+1] > N[i]:
            i += 1
        while i < len(N) - 1 and N[i+1] < N[i]:
            i += 1
        if i == len(N) - 1:
            return True
        
        return False
        
    visited = set()
    Queue = deque()
    Queue.append((0, N))
    
    while len(Queue) > 0:
        step, N = Queue.popleft()
        if test(N): return step
        for i in range(0, len(N) - 1):
            M = N[:]
            M[i], M[i+1] = M[i+1], M[i]
            if tuple(M) not in visited:
                visited.add(tuple(M))
                Queue.append((step + 1, M))
    
    



def solve(Problem, Prep):
    def transpose(S, i, j):
        count = 0
        for f in range(i, j):
            #print S[f],
            for t in range(f+1, j):
                if S[f] > S[t]: count += 1
        #print
        return count

    def transposeback(S, i, j):
        count = 0
        for f in range(i, j):
            #print S[f],
            for t in range(f+1, j):
                if S[f] < S[t]: count += 1
        #print
        return count
        
    
    
    N = Problem
#    maxN = max(N)
#    imaxN = N.index(maxN)
    
    best = 2000 * len(N)
    
#    N.remove(maxN)
    
    #print N
    
    for i in range(0, len(N)+1):
    
        A = transpose(N, 0, i)
        B = transposeback(N, i, len(N))

        #print i, A, B
        
        if A+B < best:
            best = A+B
    
    
    if len(N) == 1:
        assert (best == 0)
    
    #print best, brute(N)
    #assert best == brute(N)
    
    return brute(N)


if __name__ == "__main__":
    doit(preprocess, readinput, solve, MultiCore = True, Verify = False, Input = SMALL, Filename = None, Problem = "B", Attempt = 4)
