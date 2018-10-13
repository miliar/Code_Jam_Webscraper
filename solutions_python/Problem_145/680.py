from fractions import Fraction, gcd
from math import log, floor
import itertools
import sys

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

def parse_case(in_file):
    f = in_file.readline()
    if not f:
        raise StopIteration()
    P,Q = map(int, f.split('/'))
    return Fraction(P,Q)

def parse_file(in_file):
    N = in_file.readline()
    while in_file:
        yield parse_case(in_file) 

def run_case(case):
    p,q = case.numerator, case.denominator
    g = log(q,2)
    if int(g) != g:
        return "impossible"
    max_gens_with_pure = floor(log(p,2))
    return int(g - max_gens_with_pure)
    
if len(sys.argv) < 2:
    exit();
    
with open(sys.argv[1], 'r') as in_file:
    for n, case in enumerate(parse_file(in_file), start=1):
        print "Case #{0}: {1}".format(n, run_case(case))
