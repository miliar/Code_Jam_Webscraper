#!/usr/bin/env python

def solve():
    n, p = map(int, raw_input().split())
    g = map(lambda gi: gi % p, map(int, raw_input().split()))
    count = {0:0, 1:0, 2:0, 3:0}
    for gi in g:
        count[gi] += 1
    if p == 2:
        return count[0] + (count[1]+1)/2
    elif p == 3:
        mini = min(count[1], count[2])
        cnt = count[0] + mini
        count[1] -= mini
        count[2] -= mini
        cnt += (count[1]+2)/3 + (count[2]+2)/3
        return cnt
    else:
        mini = min(count[1], count[3])
        cnt = count[0] + mini + count[2]/2
        count[1] -= mini
        count[3] -= mini
        count[2] %= 2
        p = 1 if count[1]>0 else 3
        if count[2] == 0:
            cnt += (count[p]+3)/4
        else:
            cnt += 1 if count[p] <= 2 else (count[p]-2 +3)/4 + 1
        return cnt

T = int(raw_input())
for i in range(T):
    ans = solve()
    print "Case #%d: %d" % (i+1, ans)
