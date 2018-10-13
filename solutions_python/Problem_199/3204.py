#! /usr/bin/env pypy
#
# author: cy7M4KDaktRcoK8aznGukLJpDtI

import sys
from itertools import chain

MP = 0

def solve(args):
    print("# args: " + repr(args))
    def nodelist(t):
        r = []
        for i in xrange(len(t)-1):
            if t[i] != t[i+1]: r.append(i+1)
        print("# nodelist: " + repr(r))
        return r
    def consume(itr):
        itr = iter(itr)
        while 1:
            try:
                itm = itr.next()
            except StopIteration:
                break
        try:
            data = iter(itm)
            itr = itertools.chain(data, itr)
        except:
            yield item
    d = {}
    def flip(a, k, p, i, l, s9, d=d):
        print("#a: " + repr(a))
        for pos in xrange(p, p+k+1):
            if a[pos] == "+": a[pos] = "-"
            else: a[pos] = "+"
            s = "".join(a)
            if s == s9:
                yield i
            i_ = d.get(s)
            if i_ is None or i < i_: d[s] = i
            else: return
            l2 = l[:]
            if p in l and a[p] == a[p-1]: l2.remove(p)
            if p+k in l and a[p+k] == a[p+k-1]: l2.remove(p+k)
            # flipopts1 = (_ for _ in l2 if _+k <= len(a))
            # flipopts2 = (_-k for _ in l2 if _>=k)
            # flipopts = set()
            # (flipopts.add(_) for _ in chain(flipopts1, flipopts2))
            flipopts1 = [_ for _ in l2 if _+k <= len(a)]
            flipopts2 = [_-k for _ in l2 if _>=k]
            flipopts = set(flipopts1 + flipopts2)
            yield (flip(a[:], k, _, i+1, l2, s9, d=d) for _ in flipopts)
    (s, k) = args; k = int(k)
    if set(s) == set(["+"]): return 0
    s0 = '+' * len(s)
    l = nodelist(s)
    print("#nodelist_: " + repr(l))
    flipopts1 = [_ for _ in l if _+k <= len(s)]
    flipopts2 = [_-k for _ in l if _>=k]
    flipopts = set(flipopts1 + flipopts2)
    print("#flipopts: " + repr(flipopts))
    riter = (flip(list(s0), k, _, 1, l, s, d=d) for _ in flipopts)
    for x in chain.from_iterable(riter):
        if x is None: continue
        for xx in chain.from_iterable(iter(x)):
            if xx is not None: print(x)


n = int(sys.stdin.readline().strip())
arglist = (sys.stdin.readline().strip().split() for _ in xrange(n))

if MP:
    import multiprocessing
    mpool = multiprocessing.Pool(4)
    reslist = mpool.imap(solve, arglist)
else:
    reslist = (solve(_) for _ in arglist)

for i, r in enumerate(reslist):
    print("Case #{}: {}".format(i+1, r))

