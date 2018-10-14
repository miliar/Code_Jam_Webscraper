#! /usr/bin/env python
import sys 
import math
from decimal import *

# parsing input for a case
def read_line(f):
    line = f.readline()
    arr = line.split()
    return arr

def read_line_int(f):
    arr = read_line(f)
    t = [int(i) for i in arr]
    return t

def read_line_float(f):
    arr = read_line(f)
    t = [float(i) for i in arr]
    #t = [Decimal(i) for i in arr]
    return t


     
# to have a nice name
def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]

# number farms
def num_farms(c,f,x):
    n0 = x/c - 2.0/f
    if n0 > 0 :
        return math.floor(n0)
    else :
        return 0.0
# time with N farms (N is a float)

# time building N farms (N is an integer)
def time_farms (n,c,f) :
    times = [c/(2.0 + i*f) for i in range(n)]
    #print "%d farms" %(n)   
    #print times
    return sum(times)

# time building cookies (N is a float)
def time_cookies (n,f,x) :
    #print "time cookies "
    #print n,f
    res = x/(2.0 + n*f)
    #print res
    return res

def time (n, c,f,x):
    return (time_farms(int(n),c,f) + time_cookies(n,f,x))


# problem solver
def solver(c,f,x):
    n = num_farms(c,f,x)
    #print n
    return time(n,c,f,x)

# main program for a case
def caseprocess(f,i):
    data = read_line_float(f)
    c = data[0]
    fa = data[1]
    x = data[2]
    #print data
    #print c,fa,x
    res = solver(c,fa,x)
    return "Case #%d: %f" % (i+1,res)

# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
    f = open(input,'r')
    t1 = read_line_int(f)
    T = t1[0]
    #print "nb of cases :%d\n" % T
    o = open(output,'w')
    for i in range(T):
        #print "case number %d processed\n" % i
        oline = caseprocess(f,i)
        print oline
        o.write(oline)
    o.close()
    f.close()


