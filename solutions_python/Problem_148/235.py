import sys # standard Python library
import itertools # standard Python library
#from PerfectAllocation import PerfectAllocation # http://pastebin.com/5sv1quf0
from operator import itemgetter # standard Python library
import bisect # standard Python library
import math # standard Python library
import copy # standard Python library
from collections import deque
from fractions import gcd # standard Python library
from utilities import *  # this is helper file which can be found at http://pastebin.com/5gkyim8x
#from blist import blist # add-on library which can be downloaded from https://pypi.python.org/pypi/blist/


sys.setrecursionlimit(1000) #1000 is default
Prep = []


def preprocess():
    return None
    
def readinput(Input):
    n, X = Input.readints()
    
    N = Input.readints()
    
    N.sort()
    
    N = deque(N, 1000);
       
    return N, X

def solve(Problem, Prep):
    N, X = Problem
    
    count = 0
    while len(N) > 0:
        count += 1
        if N[-1] + N[0] <= X and len(N) > 1:
            N.popleft()
            N.pop()
            continue
        N.pop()
    
    return count
         

    return 0


if __name__ == "__main__":
    doit(preprocess, readinput, solve, MultiCore = False, Verify = False, Input = SMALL, Filename = None, Problem = "A", Attempt = 0)
