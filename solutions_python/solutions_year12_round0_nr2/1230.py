#!/usr/bin/env python
from functools import wraps

def memoized(f):
    known = dict()
    def f_prime(x):
        if x not in known: 
            known[x] = f(x)
        return known[x]
    return f_prime

@memoized
def possible_triplets(n):
    max = n//3 + 2 # can't go higher without violating max-min <= 2
    all_solutions = [(max - i, max - j, n - (max - i) - (max - j)) \
            for i in range(3)\
            for j in range(i,3)]
    return [(x,y,z) for x,y,z in all_solutions if \
                10 >= x >= y >= z >= 0 and x - z <= 2]

@memoized
def categorized_triplets(n):
    "(unsurprising, surprising)"
    return (
            filter(lambda t: max(t) - min(t) < 2, possible_triplets(n)),
            filter(lambda t: max(t) - min(t) == 2, possible_triplets(n)))

def maxmax_or_none(t):
    if t == []: return None
    return max(max(k) for k in t)
@memoized
def highest(n):
    "(unsurp, surp)"
    unsurp, surp = categorized_triplets(n)
    return (maxmax_or_none(unsurp), maxmax_or_none(surp))

def max_over(surprising, over, data):
    choices = map(highest, data)
    # now choose the surprising things so that the most
    # elements are "tripped over" from being below `over`
    # to becoming above it.
    can_be_tripped_over = len([(x,y) for x,y in choices \
            if x < over and (y is not None and y >= over)])
    certainly_over = len([(x,y) for x,y in choices \
            if x >= over])
    return min(can_be_tripped_over, surprising)+certainly_over

def parse(s):
    lines = s.splitlines()[1:]
    d = []
    for l in lines:
        sp = l.split()
        surprising = int(sp[1])
        over = int(sp[2])
        dat = map(int,sp[3:])
        d.append((surprising, over, dat))
    return d
if __name__ == '__main__':
    format = "_ surprising over data+"
    import sys
    with open(sys.argv[1]) as f:
        experiments = parse(f.read())
#"""4
#3 1 5 15 13 11
#3 0 8 23 22 21
#2 1 1 8 0
#6 2 8 29 20 8 18 18 21""")
    for i,ex in enumerate(experiments):
        print "Case #{}: {}".format(i+1, max_over(*ex))
    #print max_over(2, 8, [20,8,18,18,21])
    #print max_over(1, 5, [15,13,11])
    #print max_over(0, 8, [23,22,21])
    #print max_over(1, 1, [8,0])
    #print max_over(2, 8, [29,20,8,18,18,21])
