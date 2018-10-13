#!/usr/bin/python2
import sys
import multiprocessing
import logging
import os
import itertools
import math
import gmpy2
import copy
import collections
import string
import scipy.stats as stats
from collections import Counter


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def recurse(Pi, specialminutes):
    """ return best time """
    longest = max(Pi.keys())
    #print Pi, Pi.keys()
    #print sorted(list(Pi.elements())), "%d+%d" % (specialminutes, longest), specialminutes + longest
    if longest <= 3:
        #print "Return3", longest+specialminutes
        return longest + specialminutes
    nb = Pi[longest]
    if nb + specialminutes >= longest:
        #print "Return4", longest+specialminutes
        return longest + specialminutes
    # split longest
    best = longest + specialminutes
    for p in primes:
        if p > longest:
            break
        if nb*(p-1) + specialminutes > longest:
            break
        #print "Cut in", p
        pic = Pi.copy()
        pic[longest/p] += (nb * (p - (longest % p)))
        if longest % p != 0:
            pic[longest/p + 1] += (nb * (longest % p))
        del pic[longest]
        res = recurse(pic, specialminutes + nb*(p-1))
        if res < best:
            best = res
    #print "return", best
    return best


def solve(casedata):
    """ Solve case """
    D, Pi = casedata
    return str(recurse(Pi, 0))


def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        D = int(sys.stdin.readline().rstrip('\n'))
        Pi = Counter(map(int, sys.stdin.readline().rstrip('\n').split()))
        casedata = [D, Pi]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    cases = parse()
    # p = multiprocessing.Pool(multiprocessing.cpu_count())
    # results = p.map(solve, cases)
    # for case, result in enumerate(results):
    #     print('Case #%d: %s' % (case + 1, result))
    #     sys.stdout.flush()

    for case, data in enumerate(cases):
        result = solve(data)
        print('Case #%d: %s' % (case + 1, result))
        #sys.stdout.flush()

    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #resultobjs = [p.apply_async(solve, [case]) for case in cases]
    #for case, resultobj in enumerate(resultobjs):
    #    print('Case #%d: %s' % (case + 1, resultobj.get()))
    #    sys.stdout.flush()
