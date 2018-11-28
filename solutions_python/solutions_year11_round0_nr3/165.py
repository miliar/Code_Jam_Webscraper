#!/usr/bin/env python
import pprint as pp

def read():
    line = raw_input() 
    line = raw_input() 
    s = line.split()
    data = [int(el) for el in s]
    return data

def to_bin(num):
    a = '{0:b}'.format(num)
    res = [int(d) for d in a]
    res.reverse()
    return res

def sum_bin(a,b):
    if len(a)>len(b):
        l = len(b)
        r = a[:]
    else:
        l = len(a)
        r = b[:]
    for i in xrange(l):
        r[i] = (a[i]+b[i])%2
    #print a,"+",b,"=",r
    return r

def run_test():
    data = read()
    N = len(data)
    d2 = [to_bin(dat) for dat in data]
    r = []
    for d in d2:
        r = sum_bin(r,d)
    if 1 in r: return "NO"
    else: return sum(data)-min(data)

def main():
    tests = int(raw_input())
    for test in xrange(tests):
        print "Case #%i: %s"%(test+1, str(run_test()))

main();
