# Code Jam 2017 Qualification round
# MichelJ
# Problem C: Bathroom Stalls

def leftmax(l):
    ll = len(l)
    maxval = -1
    for i in xrange(ll):
        if l[i] > maxval:
            maxval = l[i]
            maxi = i
    return maxi

def solve_brute(n, k):
    l = [n]
    for i in xrange(k):
        im = leftmax(l)
        m = l[im]
        lm = (m - 1) // 2
        rm = m // 2
        if rm > 0:
            if lm > 0:
                l = l[:im] + [lm, rm] + l[im + 1:]
            else:
                l[im] = rm
        else:
            l.pop(im)
    return rm, lm

from heapq import *

def solve_heap(n, k):
    h = [- n]
    heapify(h)
    for i in xrange(k):
        # print h
        m = heappop(h)
        lm = (m + 2) // 2
        rm = (m + 1) // 2
        if rm < 0:
            heappush(h, rm)
        if lm < 0:
            heappush(h, lm)
    return - rm, - lm

def split(n):
    res = []
    h = [- n]
    heapify(h)
    d = {n:1}
    def inc_todo(r, v):
        if d.has_key(r):
            d[r] += v
        else:
            heappush(h, -r)
            d[r] = v
    def pop_largest():
        r = - heappop(h)
        return r, d[r]
    while len(h) > 0:
        r, v = pop_largest()
        r1 = r // 2
        r2 = (r - 1) // 2
        if r1 > 0:
            inc_todo(r1, v)
        if r2 > 0:
            inc_todo(r2, v)
        res.append((v,r))
    return res

def solve_fast(n, k):
    res = split(n)
    i = 0
    while res[i][0] < k:
        k -= res[i][0]
        i += 1
    r = res[i][1]
    return r // 2, (r - 1) // 2

def main():
    for t in xrange(input()):
        n, k = map(int, raw_input().split())
        resmax, resmin = solve_fast(n, k)
        print "Case #%d:"%(t + 1), resmax, resmin
        
main()

from multiprocessing import Pool

def f(pair):
    return solve_heap(pair[0], pair[1])

def main_mp():
    pairs = [map(int, raw_input().split()) for _ in xrange(input())]
#    print pairs
    p = Pool(8)
    sols = p.map(f, pairs)
#    sols = map(f, pairs)
    for t, (resmax, resmin) in enumerate(sols):
        print "Case #%d:"%(t + 1), resmax, resmin

#if __name__ == '__main__':
#    main_mp()
