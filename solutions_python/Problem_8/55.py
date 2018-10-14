#!/usr/bin/python

import math
import os

def factors(n):
    l = os.popen("factor %d" % n).readline().split()[1:]
    l = [eval(x) for x in l]
    res = set()
    for i in l:
        res.add(i)
    return res

facts = {}
csets = {} #current sets

def got_good_factor(a,b,p):
    global facts
    n = facts[a].intersection(facts[b])
    for i in n:
        if i >= p:
            return True
    return False

def init_factors(a,b):
    global facts
    i = a
    while i <= b:
        facts[i] = factors(i)
        i = i+1

def init_sets(a,b):
    global csets
    i = 1
    while a+(i-1) <=b:
        csets[a+i-1] = i
        i = i+1

def merge_sets(a,b):
    global csets
    if(csets[a] == csets[b]):
        return
    m = min(csets[a],csets[b])
    csets[a] = m
    csets[b] = m


def run_case(a,b,p):
    global facts
    global csets
    facts = {}
    csets = {}
    init_factors(a,b)
    init_sets(a,b)
    i = a
    while i<b:
        j = a+1
        while j<=b:
            if got_good_factor(i,j,p):
                merge_sets(i,j)
            j = j+1
        i = i+1
    res = set()
    for x in csets.keys():
        res.add(csets[x])
    return len(res)

def read_input(filename):
    f = file(filename,"r")
    out  = file(filename+'.out','w')
    tmp = f.readline()
    N = eval(tmp)
    for i in range(0,N):
        tmp = f.readline()
        tmp = tmp.split()
        a = eval(tmp[0])
        b = eval(tmp[1])
        p = eval(tmp[2])
        res = run_case(a,b,p)
        print >> out, "Case #%d: %s" % (i+1,res)
        print  "Case #%d: %s" % (i+1,res)
    f.close()
    out.close()

if __name__ == '__main__':
    read_input('B-small-attempt0.in')
    
    


    
