'''
Created on May 7, 2016

@author: John Cornwell
'''
import operator,math,string,itertools,fractions,os
import heapq,collections,re,array,bisect,random,time,inspect
from copy import deepcopy
import multiprocessing as mp
import datetime as dt
import multiprocessing.pool as mpp
from fractions import gcd
import datetime as dt
from macpath import curdir
import sys
sys.setrecursionlimit(10000)

def lcm(a, b):
    return a * b / gcd(a, b)


# Called before solving any functions
def init(i_num, fc_in):
    return

# Parse next set of arguments
def parse_next(fc_in):
    n, k = map(int, fc_in.readline().strip().split())
    pancakes = []
    for p in range(n):
        pancakes.append(map(int, fc_in.readline().strip().split()))
        
    return n, k, pancakes,


# Solve individual instance
def solve(n, k, pancakes):
    
    pancakes = [(h, r, (2  * r * h)) for r, h in pancakes]
    pancakes = sorted(pancakes, key = lambda x: (x[1], x[2]),
                       reverse=True)
    
    
    memo = {}
    def solve(left, ind):
        
        if ind == len(pancakes):
            return 0
        if left == 0:
            return 0
        if (left, ind) in memo:
            return memo[(left, ind)]
            
        ret = max(  (pancakes[ind][2] + solve(left-1, ind+1)),
                    (solve(left, ind+1)) )

        memo[(left, ind)] = ret
        return ret
        
    solve(k, 0)
  
    ret = -1
    for i, top in enumerate(pancakes):

        tot = (top[1] ** 2) + top[2]
        
        tot += solve(k - 1, i + 1)
        #print  (top[1] ** 2), top[2], solve(k - 1, i + 1)
        ret = max(tot, ret)
    return ret * math.pi
        
        
    

def _run_main():
    # Config
    s_let = os.path.splitext(__file__)[0][-1]
    s_run = 2
    distrib = 0 # 0-single, 1-parallel, 2-lambda

    if s_run == 0:
        fc_in = open('infile.in', 'r')
    elif s_run == 1:
        fc_in = open('C:\Users\John Cornwell\Desktop\%s-small-attempt1.in' % s_let, 'r')
    elif s_run == 2:
        fc_in = open('C:\Users\John Cornwell\Desktop\%s-large.in' % s_let, 'r')
    elif s_run == 3:
        fc_in = open('C:\Users\John Cornwell\Desktop\%s-small-practice.in' % s_let, 'r')
    elif s_run == 4:
        fc_in = open('C:\Users\John Cornwell\Desktop\%s-large-practice.in' % s_let, 'r')
    fc_out = open('out.txt', 'w')

    i_num = int(fc_in.readline())
    init(i_num, fc_in)

    dt_start = dt.datetime.now()
    # Parse and solve test cases
    if distrib == 0:
        for i in range(1, i_num+1):
            args = parse_next(fc_in)
            ret = solve(*args)
            s_line = 'Case #%i: %s' % (i, str(ret))
            print s_line
            fc_out.write(s_line + '\n')
    # Run jobs in parallel
    elif distrib == 1:
        new_pool = mp.Pool()
        results = []
        for i in range(1, i_num+1):
            args = parse_next(fc_in)
            results.append(new_pool.apply_async(solve, args))
        for i, r in enumerate(results):
            ret = r.get()
            s_line = 'Case #%i: %s' % (i + 1, str(ret))
            print s_line
            fc_out.write(s_line + '\n')
    # Run jobs in parallel in the cloud
    elif distrib == 2:
        new_pool = mpp.ThreadPool(900)
        results = []
        for i in range(1, i_num+1):
            args = parse_next(fc_in)
            results.append(new_pool.apply_async(lambda_post,
                                                kwds={'func': solve,
                                                      'args': args}))
        for i, r in enumerate(results):
            ret = r.get()
            s_line = 'Case #%i: %s' % (i + 1, str(ret))
            print s_line
            fc_out.write(s_line + '\n')
    print dt.datetime.now() - dt_start, 'total runtime'
    print fc_in



if __name__ == '__main__':
    _run_main()