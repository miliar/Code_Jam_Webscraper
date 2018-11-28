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

def solve_rec(pancakes):
    printd(pancakes)
    pancakes = sorted(pancakes)
    max = pancakes[-1]
    if max > 3:
        printd("moving pancakes", pancakes)
        diff_l = 1
        diff_r = int(pancakes[-1] / 2)
        t_times = []

        if diff_l <= diff_r:
            for i in xrange(diff_l, diff_r + 1):
                printd("testing" ,i)
                if i < 2:
                    continue

                pancakes[-1] -= i

                #move to another with emptier dish
                if len(pancakes) > 1 and pancakes[0] + i < pancakes[-1]:
                    pancakes[0] += i

                    t = solve_rec(pancakes) + 1
                    t_times.append(t)
                    pancakes[0] -= i

                # move to a new one
                pancakes.append(i)
                t = solve_rec(pancakes) + 1
                t_times.append(t)
                pancakes = pancakes[:-1]

                pancakes[-1] += i

        if len(t_times) > 0:
            t = min(max, min(t_times))
        else:
            t = max
        return t
    else:
        printd("p", pancakes, "not moved", "max", max)
        return max


def solver(pancakes):
    m = max(pancakes)
    t = solve_rec(pancakes)
    return t

def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    d = in_file.getInt()
    pancakes = in_file.getInts()

    return {
        'pancakes': pancakes
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
