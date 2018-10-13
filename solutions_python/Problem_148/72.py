#!/usr/bin/pypy

def solve():
    N, X = map(int,raw_input().split())
    S = map(int,raw_input().split())
    S.sort()
    res = 0
    S = list(reversed(S))
    while S:
        s = S.pop(0)
        for s2 in S:
            if s2 + s <= X:
                S.remove(s2)
                break
        res += 1
    return res

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1,T+1):
        print "Case #%d: %d"%(t,solve())
