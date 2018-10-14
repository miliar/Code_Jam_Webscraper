#!/usr/bin/python

import sys, decimal

T = int(raw_input())
tt = max(T/10, 1)

for c in xrange(T):
    print 'Case #{}:'.format(c+1),
    if c % tt == 0:
        print >>sys.stderr, 'Solving: ', (c+1)*100/T, '%'
    
    N = int( raw_input() )
    
    m = [ raw_input() for cc in xrange(N) ]

    mm = []
    count = 0
    for i in xrange(N):
        mm.append([ [0,m[i][0]] ])
        for char in m[i]:
            if char == mm[i][ -1 ][1] :
                mm[i][ -1 ][0] += 1
            else:
                mm[i].append( [1,char] )
    
    
    # print >>sys.stderr, m
    # print >>sys.stderr, mm

    leng = len(mm[0])
    flag = False
    for j in xrange(1, N):
        if len(mm[j]) != leng:
            print 'Fegla Won'
            flag = True
            break
            
    if flag:
        # print >>sys.stderr, "Length not correct"
        continue

    for i in xrange(leng):
        for j in xrange(1,N):
            if mm[0][i][1] != mm[j][i][1]:
                print 'Fegla Won'
                flag = True
                break
        if flag:
            break
            

    if flag:
        # print >>sys.stderr, "Letters are wrong"
        continue
     
    mid = []
    for i in xrange(leng):
        midd = 0
        for j in xrange(N):
            midd += mm[j][i][0]
        mid.append(midd)    
        
    mid = map( lambda x: int( round(decimal.Decimal(x)/N) ), mid )
    # Count minimum
    
    minn = 0
    for i in xrange(N):
        for j in xrange(leng):
            minn += abs(mid[j] - mm[i][j][0])
            
    print minn








