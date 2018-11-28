from __future__ import division
from functools32.functools32 import lru_cache
import sys
import itertools
import os
import re
import string
import math
import sys
import heapq
from collections import namedtuple, defaultdict, deque
from Tools import gcj
from Tools.gcj import printd
from bitstring import BitArray, BitStream
from copy import deepcopy
from simpleai.search import SearchProblem, astar
import random
import operator
#from Tools import primes

def is_valid_seq(a):
    prev = None
    lower = True
    for v in a:
        if prev is not None and lower and prev > v:
            lower = False
            prev = v
            continue
        if prev is not None and not lower and prev < v:
            return False
        prev = v
    return True

def num_swaps(a, p):

    a_pos = dict()
    order = []
    for i in xrange(len(p)):
        a_pos[p[i]] = i

    for i in xrange(len(p)):
        v = a[i]
        p = a_pos[v]
        order.append(p)

    c = 0
    for i in xrange(len(order)):
        for j in xrange(len(order)):
            if i < j and order[i] > order[j]:
                c += 1
    return c



def num_swaps_wrong(a, p):
    if a == list(p):
        return 0

    a_pos = dict()
    for i in xrange(len(p)):
        a_pos[p[i]] = i
    #printd("a", a, "p", p, "pos", a_pos)

    swaps = 0
    while True:
        #if max_swaps is not None and swaps > max_swaps:
        #    return max_swaps
        swapped = False
        for i in xrange(len(a) - 1):
            v = a[i]
            if i < a_pos[v]:
                #printd("before", a)
                a[i], a[i+1] = a[i+1], a[i]
                #printd("swap", i, i+1, a)

                swapped = True
                swaps += 1
        if not swapped:
            break
    #printd("end", a, p, swaps)
    return swaps




def solver(a):
    perms = itertools.permutations(a)

    min_swaps = None
    for p in perms:
        if is_valid_seq(p):
            printd("EVALUATING", a, p)
            s = num_swaps(list(a), p)
            printd("RESULT: ", s, "perm", p)

            if min_swaps is None or s < min_swaps:
                #printd("THIS IS LOWER", s, p)
                min_swaps = s
    return min_swaps


def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    n = in_file.getInt()
    a = in_file.getInts()
    return {
        'a': a,
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
