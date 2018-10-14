#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def possible_min_points(t):
    return [(p/3,t-p) for p in range(t,max(-1,t-5),-1) if p%3==0] 

def possible_max_points(a, A):
    # returns (max_points, is_suprise ? 1 : 0)
    if A==0:
        return [(a,0)]
    elif A==1:
        return [(a+1,0)]
    elif A==2:
        return [(a+1,0),(a+2,1)]
    elif A==3:
        return [(a+2,1)]
    else:
        assert A==4
        return [(a+2,1)]

def has_no_suprise_variant(pv,pmax):
    for p in pv:
        if p[0] >= pmax and p[1]==0:
            return True
    return False

def solve(S,pmax,T):
    #print 'solving problem: %d suprises, and t_i >= %d' % (S,pmax)
    
    N = 0
    
    minP = [possible_min_points(t) for t in T]
    #print minP

    maxP = []
    for pv in minP:
        A = []
        for p in pv:
            A.extend(possible_max_points(p[0], p[1])) 
        maxP.append(A)
    #print maxP
        
    suprise = []
    for pv in maxP:
        if has_no_suprise_variant(pv,pmax):
            N += 1
        else:
            suprises = [p for p in pv if p[1]==1]
            if suprises:
                suprise_points = map(lambda p: p[0], suprises)
                suprise.append(max(suprise_points))
    
    Np = sum(1 for points in suprise if points>=pmax)
    N += min(S,Np)
            
    return N 


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d) if len(s.strip())>0]


T = int(ifs.readline())
for t in range(1,T+1):
    A = numbers_from_line()
    N = A[0]
    S = A[1]
    p = A[2]
    P = A[3:3+N]
    a = solve(S,p,P)
    ofs.write('Case #%d: %d\n' % (t,a))
