#!/usr/bin/env python
import sys
def Take(k, gs, i):
    'Memoize this.'
    queue = gs[i:] + gs[:i]
    taken = 0
    N = len(gs)
    f = 0
    while k and f < N:
        next_group = queue[f]
        if next_group > k:
            break
        k -= next_group
        taken += next_group
        f += 1
    return taken, f+i
def Euros(R, k, gs):
    i = 0
    euros = 0
    N = len(gs)
    _done = dict()
    while R:
        if i not in _done:
            _done[i] = Take(k, gs, i)
        (taken, i) = _done[i]
        if taken == 0:
            # We can go no further!
            return euros
        #print taken, i
        euros += taken
        i = i % N
        R -= 1
    return euros
def main():
    it = iter(sys.stdin)
    T = int(next(it))
    for x in range(1, T+1):
        R, k, N = map(int, next(it).split())
        gs = map(int, next(it).split())
        assert len(gs) == N
        y = Euros(R, k, gs)
        print "Case #%d: %d" %(x, y)
            

if __name__=='__main__':
    main()
