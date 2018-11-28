#!/usr/bin/env pypy3
"""Task #1"""

def s(back, forw, dest):
    if forw[1] >= back[1]: return back[1]
    diff = forw[0] - back[0]
    meet = forw[0] + (diff*forw[1] / (back[1]-forw[1]))
    if meet >= dest: return back[1]
    left = dest - forw[0]
    return ((left*forw[1]+diff*forw[1]) / left)


for case in range(1, int(input()) + 1):

    dest, h = (int(x) for x in input().split())
    hs = []
    for _ in range(h): hs.append(tuple(int(x) for x in input().split()))

    hs.sort()
    hs.insert(0, (0, 10**20))

    while len(hs) > 1:
        f = hs.pop()
        b = hs.pop()
        hs.append((b[0], s(b, f, dest)))




    print('Case #{}: {}'.format(str(case), str(hs[0][1])))
