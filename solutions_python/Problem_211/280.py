# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
import numpy as np
import itertools
from scipy.optimize import minimize

def parse(f):
    lst = []
    f.next()
    for l1 in f:
        N = int(l1.split()[0])
        K = int(l1.split()[1])
        l2 = f.next()
        U = float(l2)
        l3 = f.next()
        Ps = [float(p) for p in l3.split()]
        lst.append((N, K, U, Ps))
    return lst


def proba_failure(N, K, Ps):
    # idx = range(N)
    # som = 0
    # for L in range(K, N+1):
    #     for subs in itertools.combinations(idx, L):
    #         p = 1
    #         for i in idx:
    #             p *= (Ps[i] if i in subs else (1-Ps[i]))
    #         som += p
    # return (1-som)
    p = 1.
    for a in Ps:
        p *= a
    return (1-p)

def core(N, K, U, Ps):
    x0 = np.array([U/N]*N)
    cons = [dict(), dict(), dict()]
    cons[0]['type'] = 'ineq'
    cons[0]['fun'] = lambda x: np.array([U - sum(x)])
    cons[1]['type'] = 'ineq'
    cons[1]['fun'] = lambda x: np.array(x)
    cons[2]['type'] = 'ineq'
    cons[2]['fun'] = lambda x: np.array([1 - Ps[i] - x[i] for i in range(N)])

    
    res = minimize((lambda x: proba_failure(N, K, [Ps[i] + x[i] for i in range(N)])), x0, constraints=cons,
                    method='COBYLA',
                   options={'catol': 1e-10, 'maxiter': 10000000})

    return (1 - proba_failure(N, K,  [Ps[i] + res.x[i] for i in range(N)]))

def output(fw, inlst):
    for i, a in enumerate(inlst):
        ret = core(*a)
        # print(i, a)
        print(i, ret)
        fw.write("Case #" + str(i+1) + ": " + str(ret)+ "\n")


f = open("C.in", 'r')
fw = open("C.out", 'w')
output(fw, parse(f))
