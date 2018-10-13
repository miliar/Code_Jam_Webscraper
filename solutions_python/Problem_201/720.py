from itertools import *
from functools import *
from operator import *
from math import *
from collections import Counter
import heapq

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

filename = "C-large"
result_string = "Case #{}: {}"

def S(N):
    # 2 -> 0 1
    # 3 -> 1 1
    # 4 -> 1 2
    # 5 -> 2 2
    if N%2==0:
        return ((N-1)/2, N/2)
    else:
        return ((N-1)/2, (N-1)/2)

def prio(sl, sr):
    return (-1*min(sl, sr), -1*max(sl, sr))


def main(input_filename, output_filename):
    with open(input_filename) as input, open(output_filename, 'w') as output:
        T, = nis(input)
        for t in range(T):
            N,K = nis(input)
            # print(N)
            # sn = S(N)
            # # h = [(prio(*sn), N)]
            # h = [-N]
            # for k in range(K):
            #     # m, n = h[0] #heapq.heappop(h)
            #     n = -h[0]
            #     # h = h[1:]
            #     # # print("gluglu", m, n)
            #     sl, sr = S(n)
            #     heapq.heapreplace(h, -sl)
            #     heapq.heappush(h, -sr)


            # print(max(sr, sl), min(sr, sl))
            # print(m)
            o = opt(N, K-1)
            sr, sl = S(o)
            # print(S(o))
            # print(o)
            # print(max(S(o)), min(S(o)))
            w(output, t, "{} {}".format(max(sr, sl), min(sr, sl)))


def w(output, i, res):
    print result_string.format(i+1, res)
    output.write(result_string.format(i+1, res)+'\n')

def sis(input):
    return input.readline().split()

def nis(input):
    return map(int, input.readline().split())

def integer_sqrt(i):
    """return tuple (s, b), where b is true if and only if i is a perfect square
    and s is the integer square root
    """
    if not i: return 0
    if i < 0: raise ValueError("cannot calculate square root of negative")
    def n(xn):
        return (xn + i/xn)/2
    xn, xnp, xnpp = i, n(i), n(n(i))
    while xn != xnpp:
        xn, xnp, xnpp = xnp, xnpp, n(xnpp)
    return min(xnp, xnp)

class Memoize(object):
    def __init__(self, f):
        self.f = f
        self.memory = {}
    def __call__(self, *args, **kwargs):
        if (tuple(args), tuple(kwargs.items())) in self.memory:
            return self.memory[(tuple(args), tuple(kwargs.items()))]
        else:
            val = self.f(*args, **kwargs)
            self.memory[(tuple(args), tuple(kwargs.items()))] = val
            return val

@Memoize
def opt(N, K):
    if K == 0: return N
    else:
        sl, sr = S(N)
        lk, lr = S(K)
        return max(opt(sl, lk), opt(sr, lr))

if __name__ == '__main__':
    input_filename = "{}.in".format(filename)
    output_filename = "{}.out".format(filename)
    main(input_filename, output_filename)
