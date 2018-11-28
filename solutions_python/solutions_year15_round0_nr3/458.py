#!/usr/bin/env python
import fileinput
import itertools
f = fileinput.input()
T = int(f.readline())
#p = "ijkijkijki" * 1000
#k = itertools.repeat(p,1000000000000)
#q2n = { 0:(1, 1), 1:(1, 'i'), 2:(1, 'j'), 3:(1, 'k'), 4:(-1, 1), 5:(-1, 'i'), 6:(-1, 'j'), 7:(-1, 'k') }
#n2q = dict (zip(q2n.values(),q2n.keys()))
#print q2n
#print n2q
table = {
        '11':(1, '1'), '1i':(1, 'i'), '1j':(1, 'j'), '1k':(1, 'k'), 
        'i1':(1, 'i'), 'ii':(-1, '1'), 'ij':(1, 'k'), 'ik':(-1, 'j'), 
        'j1':(1, 'j'), 'ji':(-1, 'k'), 'jj':(-1, '1'), 'jk':(1, 'i'), 
        'k1':(1, 'k'), 'ki':(1, 'j'), 'kj':(-1, 'i'), 'kk':(-1, '1')
        }
def tr(an, aq, bn, bq):
    cn, cq = table[aq+bq]
    #print 'tr', an, aq, '*', bn, bq, '=', an * bn * cn, cq
    return (an * bn * cn, cq)

def findijk(S):
    n = 1
    x = '1'
    while x!='i': 
        y = next(S)
        n,x = tr(n, x, 1, y)
    x = '1'
    while x!='j': 
        y = next(S)
        n,x = tr(n, x, 1, y)
    x = '1'
    while x!='k': 
        y = next(S)
        n,x = tr(n, x, 1, y)
    return n, S

def reducestr(S):
    n = 1
    x = '1'
    try:
        while 1: 
            y = next(S)
            n,x = tr(n, x, 1, y)
    except StopIteration:
        return n, x
    
def solve(l,s,x):
    S = iter(s * x)
    if l*x < 3: return 'NO';
    try:
        n, S = findijk(S)
        n2, c = reducestr(S)
        #print 'leave', n*n2, c
        if n*n2==1 and c == '1':
            return 'YES'
    except StopIteration:
        pass
        #print 'StopIteration'
    return 'NO'

for t in range(T):
    [l,x] = f.readline().strip().split()
    s = f.readline().strip()
    l = int(l)
    x = int(x)
    #print l, s, x
    ans = solve(l, s, x)
    print 'Case #{}: {}'.format(t+1, ans)
