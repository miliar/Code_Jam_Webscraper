'''
Created on 22 maj 2011

@author: rickard
'''
import sys
def extent(s, i):
    j = i
    while j<len(s) and s[i] == s[j]: j+= 1
    return j-i

def solve(l):
    for r in range(len(l)-1):
        for c in range(len(l[r])-1):
            if l[r][c] == '#':
                xt = extent(l[r],c)
                if xt % 2 == 0:
                    for cc in range(c,c+xt):
                        l[r][cc] = '/\\'[(cc-c)%2]
                        if l[r+1][cc] != '#':
                            return "Impossible"
                        else:
                            l[r+1][cc] = '\\/'[(cc-c)%2]
                else: return "Impossible"
    if any('#' in r for r in l): return "Impossible"
    return '\n'.join(map(lambda x:''.join(x),l))


T = int(sys.stdin.readline())
for c in range(1,T+1):
    R,C = map(int, sys.stdin.readline().split())
    l = [sys.stdin.readline().strip() for _ in range(R)]
    l = map(list, l)
    print "Case #%d:" % c
    print solve(l)