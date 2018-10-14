#!/usr/bin/env python

def verify():
    pass

def solve(D,N):
    horses=[raw_input().split() for _ in range(N)]
    horses.sort(reverse=True)
    worst=0.0
    for horse in horses:
        time_to_finish = (D-int(horse[0]))/float(horse[1])
        if time_to_finish > worst:
            worst = time_to_finish
    return D/worst

t = int(raw_input())
for cas in xrange(1,t+1):
    ans = solve(*map(int,raw_input().split()))
    print "Case #{}: {}".format(cas,ans)
