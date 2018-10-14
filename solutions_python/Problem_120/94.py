""" imports """
import glob, pprint, pickle, os, time, sys
from copy import copy
from numpy import array, sin, cos, sqrt

""" global variables """

""" classes """

""" functions """
def T(r, N):
    return (2*r-1)*N + 2*N**2

def solve(r, t):
    if r > 1000000:
        r, t = float(r), float(t)
        ra = 2*r-1
        Delta_a = 1 + 8*t/ra**2
        Nhat = (ra * (sqrt(Delta_a) - 1))/4
    else:
        r, t = float(r), float(t)
        Delta = (2*r - 1)**2 + 8*t
        Nhat = (-(2*r-1) + sqrt(Delta))/4
    N = int(Nhat) if Nhat > 1 else 1
    print "------N={}--------".format(N)
    print T(r,N), t , T(r, N+1)
    assert T(r,N) <= t < T(r, N+1)
    return N

""" parse input """
output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):
        ### parse input ###
        r, t = read_ints()
        ### calculate answer ###
        answer = solve(r, t)
        ### output ###
        # print "Calculating case #{}...".format(questionindex+1)
        answer_str = "Case #{}: {}".format(questionindex+1, answer)
        output += answer_str + '\n'
        print answer_str
ofile = open('output', 'w').write(output)
TOC = time.time()
print "done in {} s".format(TOC-TIC)