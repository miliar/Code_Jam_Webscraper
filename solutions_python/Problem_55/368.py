#!/usr/bin/env python

INFILENAME = 'C-large.in'
OUTFILENAME = 'output.out'

def initIO():
    read = open(INFILENAME, 'rt')
    write = open(OUTFILENAME, 'wt')
    return (read, write)

def deinitIO(read, write):
    read.close()
    write.close()

def prepare(k, g):
    ng = []
    for x in xrange(len(g)):
        p = 0
        shift = len(g)
        for s in xrange(len(g)):
            cg = g[(x+s)%len(g)]
            if (p+cg > k):
                shift = s
                break
            p += cg
        ng.append( (p, shift) )
    return ng

def findLoopStart(ng):
    visited = {}
    curr = 0
    iter = 0
    cost = [0]
    while True:
        if curr in visited:
            return (curr, iter-visited[curr], cost[-1] - cost[visited[curr]])
            
        visited[curr] = iter
        
        cost.append(cost[-1] + ng[curr][0])
        curr = (curr + ng[curr][1])%len(ng)
        iter += 1

def solve(case, r, w):
    [R, k, N] = [int(x) for x in r.readline().split()]
    g = [int(x) for x in r.readline().split()]
    
    if (len(g) != N):
        print 'Warning: G != N.'
        
    ng = prepare(k, g)
    
    (ls, ll, lc) = findLoopStart(ng)
    money = 0
    curr = 0
    
    while R>0 and curr != ls:
        R -= 1
        money += ng[curr][0]
        curr = (curr + ng[curr][1])%len(ng)
    
    money += (R/ll)*lc
    R = R%ll
    
    while R>0:
        R -= 1
        money += ng[curr][0]
        curr = (curr + ng[curr][1])%len(ng)
        
    w.write( 'Case #{0}: {1}\n'.format(case, money) )

def main():
    r, w = initIO()
    
    T = int(r.readline())
    current = 1
    
    while (T>0):
        solve(current, r, w)
        
        T -= 1
        current += 1
        
    
    deinitIO(r, w)

main()