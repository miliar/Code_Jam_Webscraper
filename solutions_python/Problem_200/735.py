from itertools import *
from functools import *
from operator import *
from math import *
from collections import Counter

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

filename = "B-large"
result_string = "Case #{}: {}"

def tidy(N):
    N = map(int, str(N))
    return all(map(lambda a: a[0]<=a[1], zip(N, N[1:])))

def numlist(N):
    return map(int, str(N))

def main(input_filename, output_filename):
    with open(input_filename) as input, open(output_filename, 'w') as output:
        T, = nis(input)
        for t in range(T):
            N, = nis(input)
            # print(N)
            for i in range(len(str(N))-2, -1, -1):
                NL = numlist(N)
                # print(NL[i], NL[i+1])
                if NL[i] > NL[i+1]:
                    NL = NL[:i+1] + [0] * (len(NL) - i -1)
                    N = int(''.join(map(str, NL))) - 1
                    # print("new",N)
            # res = ''.join(map(str, l[::-1]))
            w(output, t, N)


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


if __name__ == '__main__':
    input_filename = "{}.in".format(filename)
    output_filename = "{}.out".format(filename)
    main(input_filename, output_filename)
