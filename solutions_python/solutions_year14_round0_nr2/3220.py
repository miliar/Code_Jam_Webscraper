from decimal import Decimal, getcontext
import sys
import math
import time

import time
from contextlib import contextmanager

# @contextmanager
# def measureTime(title):
#     t1 = time.clock()
#     yield
#     t2 = time.clock()
#     print '%s: %0.2f seconds elapsed' % (title, t2-t1)

@contextmanager
def measureTime(title):
    # t1 = time.clock()
    yield
    # t2 = time.clock()
    # print '%s: %0.2f seconds elapsed' % (title, t2-t1)

getcontext().prec = 15
import sys
from collections import defaultdict

def read_int():
    return int(raw_input())

def read_line():
    return sys.stdin.readline().rstrip("\n")

def read_int_line(num):
    l = [Decimal(x) for x in read_line().split()]
    assert len(l) == 4
    return l

def read_table():
    return [read_int_line(4),
            read_int_line(4),
            read_int_line(4),
            read_int_line(4)]

ncases = read_int()

for case in xrange(ncases):
    c, f, x = [Decimal(x) for x in read_line().split()]

#    print "c={}, f={}, x={}".format(c,f,x)
    i = 0
    total = 0
    limit = x/c - 2/f - 1
    d = 2
    with measureTime("finding time"):
        while 1:
            next = c / d
            to_end = x / d
            if i >= limit:
            #if next + (x/(2+f*(i+1))) > to_end:
                #print "end i={} limit={} ceil={}".format(i, limit, math.ceil(limit))
                total += to_end
                break
            total += next
            i += 1
            d += f


    print "Case #{}: {:.7f}".format(case + 1, total)
    # print

# Case #1: 7
# Case #2: Bad magician!
# Case #3: Volunteer cheated!
