#!/usr/bin/python
# coding=utf8
import sys
import math
from time import time
from itertools import permutations, combinations
import collections
import functools
from fractions import gcd, Fraction
import string
import operator
#import random (not working in python3)
import bisect
from numpy import cross, dot, multiply, add, subtract
from numpy.linalg import norm

print_realtime = len(sys.argv) == 2 and sys.argv[1] == "print_realtime"

def dbg(txt):
    sys.stderr.write(txt + "\n")


def print_var(*args):
    for var_name in args:
        assert type(var_name) == str
        calling_frame = sys._getframe().f_back
        var_val = calling_frame.f_locals.get(var_name, calling_frame.f_globals.get(var_name, None))
        dbg(var_name+'='+ str(var_val))


class timed(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        t1 = time()
        ret = self.func(*args)
        dif_time = time() - t1
        print("%s: returned %s in %f seconds" % (self.func.__name__, ret, dif_time))
        return ret


def comp(f1, f2, *args):
    t1 = time()
    r1 = f1(*args) if f1 is not None else None
    t2 = time()
    r2 = f2(*args) if f2 is not None else None
    t3 = time()
    res = "%5s: %s in %f\n%5s: %s in %f" % (f1.__name__ if f1 is not None else None, r1, t2 - t1,
                                            f2.__name__ if f2 is not None else None, r2, t3 - t2)
    if r1 != r2:
        dr = "!! DIFFERENT RESULTS !!"
        res = dr + "\n" + res + "\n" + dr
    print(res)
    return r1 if r1 == r2 else None


def alg2(D, P):
    best_res = None
    iterations = 0
    while True:
        max_p = max(P)
        cur_res = iterations + max_p
        if cur_res < best_res or best_res is None:
            best_res = cur_res
        if max_p == 1:
            break
        P.remove(max_p)
        if max_p == 9:
            sc_max = max(P) if len(P) > 0 else 0
            if sc_max <= 3:
                P += [3, 3]
                iterations += 2
                continue
        max_p_over_two = max_p // 2
        if max_p % 2 == 1:
            P.append(max_p_over_two)
            P.append(max_p_over_two + 1)
        else:
            P.append(max_p_over_two)
            P.append(max_p_over_two)
        iterations += 1

    return best_res


def best_case(P):
    if len(P) == 0:
        return 0

    eat = [x - 1 for x in P if x > 1]
    poss = [eat]

    maxP = max(P)
    newP = P
    newP.remove(maxP)
    for i in range(1, maxP // 2 + 1):
        poss.append(sorted(newP + [i, maxP - i]))

    best_score = None
    for c in poss:
        score = best_case(c)
        if score < best_score or best_score is None:
            best_score = score
    return best_score + 1


def alg3(D, P):
    # brute force
    return best_case(list(sorted(P)))

poss = {
    1: [(0, 1)],
    #2: [(0, 2), (1, 1)],
    2: [(0, 2)],
    #3: [(0, 3), (1, 2)],
    3: [(0, 3)],
    #4: [(0,4), (1,2), (2,2), (3,1)],
    4: [(0, 4), (1, 2)],
    #5: [(0, 5), (1, 3), (2, 2)],
    5: [(0, 5), (1, 3)],
    #6: [(0, 6), (1, 3), (2, 2)],
    6: [(0, 6), (1, 3)],
    #7: [(0, 7), (1, 4), (2, 3), (3, 2)],
    7: [(0, 7), (1, 4)],
    #8: [(0, 8), (1, 4), (2, 3), (3, 2)],
    8: [(0, 8), (1, 4)],
    9: [(0, 9), (1, 5), (2, 3)]
}

def test_comb(comb, P):
    div, eat = 0, 0
    for i in range(len(P)):
        pair = poss[P[i]][comb[i]]
        div += pair[0]
        eat = pair[1] if pair[1] > eat else eat
    return (div, eat)

def alg(D, P):
    comb = [0] * D
    nb_comb = [0] * D
    for i in range(D):
        nb_comb[i] = len(poss[P[i]])
    best_score = None
    while True:
        #dbg("Testing comb %s" % comb)
        # test this comb and go to the next one
        r = test_comb(comb, P)
        score = r[0] + r[1]
        if best_score is None or score < best_score:
            #dbg("best comb with %s is %s" % (score, r))
            best_score = score

        i_to_inc = 0
        while True:
            comb[i_to_inc] += 1
            if comb[i_to_inc] >= nb_comb[i_to_inc]:
                comb[i_to_inc] = 0
                i_to_inc += 1
                if i_to_inc >= D:
                    # that's it!
                    return best_score
                else:
                    continue  # next digit
            else:
                break  # ok next combo


def main():
    #import cProfile
    #cProfile.runctx('alg()', globals(), locals())
    data = sys.stdin
    nb = int(data.readline())
    #a, b = map(int,data.readline().split())
    for icase in range(nb):
        #L = list(map(float, data.readline().split()))  # float
        #L = data.readline().split()  # string
        #s = data.readline().strip()
        D = int(data.readline().strip())
        P = list(map(int, data.readline().split()))  # int
        res = alg(D, P)
        ret = "Case #%d: %s" %(icase + 1, res)
        if print_realtime:
            dbg(ret)
        print(ret)


if __name__ == "__main__":
    main()
