from __future__ import division
T = int(raw_input())
for i in range(T):
    D, N = map(int,raw_input().split())
    slow = 0
    sstart, sspeed = 0, 0
    for _ in range(N):
        start, speed = map(int, raw_input().split())
        time = (D - start)/speed
        if  slow < time:
            slow = time
            sstart = start
            sspeed = speed
    print "Case #"+str(i+1)+": "+"{:10.6f}".format(D/slow)