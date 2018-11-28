""" imports """
import glob, pprint, pickle, os, time, sys
from copy import copy
from numpy import array, sin, cos

""" global variables """

""" classes """

""" functions """
def rate(N, M, K, products, (A, B, C)):
    possibilities = [
        1,
        A, B, C,
        A*B, A*C, A*B,
        A*B*C,
    ]
    for p in products:
        if not p in possibilities:
            return 0
    r = 1
    print A, B, C, '-->', r
    return 1

def solve(N, M, K, products):
    assert N == 3 # restricting
    m = range(2, M+1)
    rates = {}
    for A in m:
        for B in m:
            for C in m:
                ABC = tuple(sorted([A,B,C]))
                if ABC in rates:
                    continue
                r = rate(N, M, K, products, (A, B, C))
                rates[ABC] = r
    return [ABC for ABC, r in rates.items() if r == max(rates.values())][0]

""" parse input """
output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    (numquestions,) = read_ints()
    assert numquestions == 1
    output = "Case #1:\n"
    (R, N, M, K) = read_ints()
    for questionindex in xrange(R):
        print "------------------ Q-----------------------"
        ### parse input ###
        products = read_ints()
        assert len(products) == K
        ### calculate answer ###
        answer = solve(N, M, K, products)
        answer_str = ''.join([str(x) for x in answer])
        print answer_str
        ### output ###
        # print "Calculating case #{}...".format(questionindex+1)
        output += answer_str + '\n'
        # print answer_str
ofile = open('output', 'w').write(output)
TOC = time.time()
# print "done in {} s".format(TOC-TIC)