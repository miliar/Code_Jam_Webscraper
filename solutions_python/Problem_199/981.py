'''
Created on May 7, 2016

@author: John Cornwell
'''
import operator,math,string,itertools,fractions,os
import heapq,collections,re,array,bisect,random,time,inspect

import datetime as dt


def lcm(a, b):
    return a * b / gcd(a, b)


# Called before solving any functions
def init(i_num, fc_in):
    return

# Parse next set of arguments
def parse_next(fc_in):
    line, num = fc_in.readline().strip().split()
    num = int(num)
    return line, num


# Solve individual instance
def solve(line, num):
    cnt = 0
    line = [x == '-' for x in line]

    for i in range(len(line) - (num - 1)):

        print i
        if line[i]:
            cnt += 1
            print i
            for j in range(i, i + num):
                line[j] = not line[j]
    if sum(line) != 0:
        return 'IMPOSSIBLE'
    
    return cnt
    

def _run_main():
    # Config
    s_let = os.path.splitext(__file__)[0][-1]
    s_run = 2
    distrib = 0 # 0-single, 1-parallel, 2-lambda

    if s_run == 0:
        fc_in = open('infile.in', 'r')
    elif s_run == 1:
        fc_in = open('C:\Users\John Cornwell\Desktop\%s-small-attempt0.in' % s_let, 'r')
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
    for i in range(1, i_num+1):
        args = parse_next(fc_in)
        ret = solve(*args)
        s_line = 'Case #%i: %s' % (i, str(ret))
        print s_line
        fc_out.write(s_line + '\n')
   


if __name__ == '__main__':
    _run_main()