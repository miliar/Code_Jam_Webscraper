#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math, string
import time
import getopt
from collections import Counter, namedtuple
from itertools import *
import operator
import multiprocessing
import os.path
from random import *
import sys
from copy import deepcopy
import pprint

printer = pprint.PrettyPrinter(indent=4)

def debug(**a): print " ".join("%s=%s" % (k,v) for (k, v) in a.iteritems())
def read_ints(): return [int(x) for x in raw_input().strip().split()]
def read_string(): return raw_input().rstrip('\r\n')

def pp(a): printer.pprint(a)
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size
def str2array(s): return [s[i] for i in xrange(0, len(s))]
def read2darry(path, func):
    ret=[]
    with open(path) as f:
        for line in f:
            line = line.rstrip()
            ret.append(map(func, [line[i] for i in xrange(0, len(line))]))
            return ret

def forall(pred, seq):  # inefficient
    return reduce(lambda r,x: r and pred(x), seq, True)

def exists(pred, seq):  # inefficient
    return reduce(lambda r,x: r or pred(x), seq, False)

def transpose(m): return map(list, zip(*m))
def uniq(seq): return list(set(seq))

def read_testcase():
    # X,Y = read_numbers()
    # Ls = read_string()
    # Coff = namedtuple("Coff", ["x_id", "count", "limit", "satisfy"])
    #  for i in xrange(N):
    #    coffs.append(Coff(*([i,] + read_numbers())))
    # del i,x, y
    first_answer = readint()
    first_cards = [read_ints() for _ in xrange(4)]
    second_answer = readint()
    second_cards = [read_ints() for _ in xrange(4)]
    return locals()

def solve(**rest):
    a1 = int(rest['first_answer'])
    a2 = int(rest['second_answer'])
    c1 = rest['first_cards'][a1-1]
    c2 = rest['second_cards'][a2-1]
    diff = list(set(c1) & set(c2))
    l = len(diff)
    if l == 1:
        return diff[0]
    elif l > 1:
        return 'Bad magician!'
    elif l == 0:
        return 'Volunteer cheated!'

def read_testcases(nr_tc):
    for i in range(nr_tc):
        yield read_testcase()

nr_tc = readint()
testcases = read_testcases(nr_tc)
specified_tc = sys.argv[1:2]

def call_solve(q):
    d = dict()
    d.update(q)
    return solve(**d)

t00 = time.clock()
MULTI = True
if specified_tc:
    stc = int(specified_tc.pop())
    testcase = [x for idx, x in enumerate(testcases) if idx == stc - 1].pop()
    print testcase
    res = solve(**testcase)
    print "Case #%d: %s" % (stc,str(res))
    sys.exit()
elif MULTI:
    p = multiprocessing.Pool()
    res = p.imap(call_solve, testcases)
else:
    res = imap(call_solve, testcases)

for (i, r) in enumerate(res, start=1):
    print "Case #%d: %s" % (i,str(r))

# for t in xrange(readint()):
#     t0 = time.clock()
#     dbg("Test #%d:" % (t+1))
#     ans = solve()
#     print "Case #%d: %d" % (t+1,ans)
#     dbg("time %.2f sec" % (time.clock() - t0))
#dbg("total time %.2f sec" % (time.clock() - t00))

