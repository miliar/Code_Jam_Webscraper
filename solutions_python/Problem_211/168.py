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

def lcm(a, b):
    return a * b / gcd(a, b)


# Called before solving any functions
def init(i_num, fc_in):
    return

# Parse next set of arguments
def parse_next(fc_in):
    n, k = map(int, fc_in.readline().strip().split())
    u = float(fc_in.readline())
    cores = map(float, fc_in.readline().strip().split())
        
    return n, k, u, cores


# Solve individual instance
def solve(n, k, u, cores):
 
    if sum(cores) + u >= n:
        return 1.0
    cores = sorted(cores, reverse=True)
    print cores       
    ret = 0.0
    for i, p in enumerate(cores):
        to_max = sum([p - x for x in cores[i+1:]])
        if to_max > u:
            continue
        u_left = u - to_max
        left = len(cores) - i
        
        first = 1.0
        for p_f in cores[:i]:
            first *= p_f
        
        p_new = min(1.0, p + (u_left / left))
        
        ret_n = first
        for _ in range(left):
            ret_n *= p_new
        print i, first, left, p_new, ret_n
        ret = max(ret, ret_n)
        
    return ret

    
    

def _run_main():
    # Config
    s_let = os.path.splitext(__file__)[0][-1]
    s_run = 1
    distrib = 0 # 0-single, 1-parallel, 2-lambda

    if s_run == 0:
        fc_in = open('infile.in', 'r')
    elif s_run == 1:
        fc_in = open('C:\Users\John Cornwell\Desktop\%s-small-1-attempt2.in' % s_let, 'r')
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