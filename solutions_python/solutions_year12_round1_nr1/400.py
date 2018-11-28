#!/usr/bin/env python2

from multiprocessing import Pool, cpu_count
from functools import partial
import operator
import pudb

pool = Pool(cpu_count())

def strat_type(pw, p, bs = 0):
    typed = len(p)
    ent = 1

    if bs == typed:
        return typed + pw + ent
    elif bs == 0:
        typed = len(p)
        right = reduce(operator.mul,p)
        wrong = 1 - right
        r_keys = ( pw - typed ) + ent
        w_keys = ( pw - typed ) + pw + 2
        return right * r_keys + wrong * w_keys
    else:
        typed = len(p) - bs
        right = reduce(operator.mul,p[:typed])
        wrong = 1 - right
        r_keys = ( pw - typed ) + ent + bs
        w_keys = ( pw - typed ) + ent + bs + pw + ent
        return right * r_keys + wrong * w_keys

def strat_redo(pw, p):
    return pw + 2

def calc_key(pw_len, prob):
    ans = []
    ans.append(strat_redo(pw_len, prob))
    for i in xrange(len(prob)+1):
        ans.append(strat_type(pw_len, prob, i))

    #print ans
    return min(ans)

nc = int(raw_input())
for c in xrange(nc):
    a,b = map(int,raw_input().split())
    prob = map(float,raw_input().split())

    ans = calc_key(b,prob)

    print "Case #%d: %.6f" % (c+1,ans)
