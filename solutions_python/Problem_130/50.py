#!/usr/bin/env python

def worst_for(n, x):
    if x == 0:
        return 1
    return 2 ** (n - 1) + worst_for(n - 1, (x - 1) / 2)

def best_for(n, x):
    people_worse = 2 ** n - 1 - x
    if people_worse == 0:
        return 2 ** n
    return best_for(n - 1, 2 ** (n - 1) - 1 - (people_worse - 1) / 2)

def solve(n, p):
    if p == 2 ** n:
        return (2 ** n - 1, 2 ** n - 1)
    lo = 0
    high = 2 ** n - 1
    # need to find worst_for(n, lo) <= p, worst_for(n, lo + 1) > p
    while lo + 1 < high:
        mid = (lo + high) / 2
        if worst_for(n,mid) <= p:
            lo = mid
        else:
            high = mid
    best = lo
    lo = 0
    high = 2 ** n - 1
    while lo + 1 < high: # need to find best_for(n, lo) <= p, best_for(n, lo + 1) > p
        mid = (lo + high) / 2
        if best_for(n,mid) <= p:
            lo = mid
        else:
            high = mid
    worst = lo
    return best, worst

        
if __name__ == "__main__":
    T = int(raw_input())
    for ncase in xrange(1, T + 1):
        n, p = map(int, raw_input().split())
        best, worst = solve(n, p)
        print "Case #%d:" % ncase, best, worst
