#!/usr/bin/python

__author__ = "Thomas van den Berg"

# from itertools import izip, permutations
# from numpy import *
from pprint import pprint

def avg(l):
    return sum(l)/float(len(l))

fn = 'A-large.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    
    N = int(f.readline())

    t    = []    
    wp   = [0] * N
    owp  = [0] * N
    oowp = [0] * N
    rpi  = [0] * N
    
    # Compute WP
    for i in xrange(N):
        t.append([None] * N)
        for (j,c) in enumerate(f.readline()):
            if c == '1':
                t[i][j] = 1
            elif c == '0':
                t[i][j] = 0
        
        games = filter(lambda x: x is not None, t[i])
        wp[i] = sum(games)/float(len(games))
    
    # Compute OWP
    owpa = []
    for i in xrange(N):
        owpa.append([0]*N)
        for j in xrange(N):
            if t[i][j] is not None:
                games = t[j][:i]+t[j][i+1:]
                games = filter(lambda x: x is not None, games)
                owpa[i][j] = sum(games)/float(len(games))
            else: 
                owpa[i][j] = None
        owpas = filter(lambda x: x is not None, owpa[i])
        owp[i] = avg(owpas)
        
    # Compute OOWP
    for i in xrange(N):
        tmp = []
        for j in xrange(N):
            if t[i][j] is not None:
                tmp.append(owp[j])
        oowp[i] = avg(tmp)
    
  
    # Final scores
    for i in xrange(N):
        rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
        

    ans = '\n' + '\n'.join('%.12f'%r for r in rpi)
    
    fout.write('Case #%d: %s\n'%(case+1,ans))
    
