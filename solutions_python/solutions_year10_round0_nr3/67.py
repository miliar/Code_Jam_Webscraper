#!/bin/python

import sys

inf = sys.stdin
T = int(inf.readline())
    
for t in range(T):
    R, k, N = map(int, inf.readline().split())
    groupsize = map(int, inf.readline().split())
    #print 'R=%d, k=%d, N=%d' % (R, k, N)
    #print 'groups', groupsize
    
    rides = []
    start2ride = {}
    ridestart = 0
    i = -1 # waiting group
    ridesize = 0
    waitsize = 0
    while waitsize <= k:
        if ridesize + waitsize > k or (i == ridestart and ridesize > 0):
#            print 'adding ride', ridesize, 'next group', i
            start2ride[ridestart] = len(rides)
            rides.append(ridesize)
            ridestart = i
            ridesize = 0
            if i in start2ride:
                break
        else:
            ridesize += waitsize
            i = (i + 1) % N
#            print 'adding more passengers', waitsize, 'now up to', ridesize, 'next group', groupsize[i]
            waitsize = groupsize[i]
    
#    print 'rides', rides
    
    startRecur = start2ride[i]
    nonrecur = rides[0:startRecur]
    recur = rides[startRecur:]
#    print 'startRecur', startRecur, 'nonrecur', nonrecur, 'recur', recur

    if waitsize > k or len(rides) == 0:
        money = sum(rides)
    else:
        if R < len(nonrecur):
            money = sum(nonrecur[0:R])
            R = 0
        else:
            money = sum(nonrecur)
            R -= len(nonrecur)
            
#        print 'summed non-recur, money=%d, R=%d' % (money, R)
        money += R / len(recur) * sum(recur)
#        print 'R/len(recur)=%d, sum(recur)=%d, money=%d' % (R/len(recur), sum(recur), money)
        money += sum(recur[:R%len(recur)])
#        print 'R%%len(recur)=%d, sum=%d, money=%d' % (R%len(recur), sum(recur[:R%len(recur)]), money)
        
    print 'Case #%d: %s' % (t+1, money)