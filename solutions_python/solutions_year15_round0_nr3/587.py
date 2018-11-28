#!/usr/bin/python3
# coding=utf8
import sys
import math
from time import time
from itertools import permutations, combinations
import collections
import functools
from fractions import gcd, Fraction
import string
import operator
#import random (not working in python3)
import bisect
from numpy import cross, dot, multiply, add, subtract
from numpy.linalg import norm

print_realtime = len(sys.argv) == 2 and sys.argv[1] == "print_realtime"

def dbg(txt):
    sys.stderr.write(txt + "\n")


def print_var(*args):
    for var_name in args:
        assert type(var_name) == str
        calling_frame = sys._getframe().f_back
        var_val = calling_frame.f_locals.get(var_name, calling_frame.f_globals.get(var_name, None))
        dbg(var_name+'='+ str(var_val))


class timed(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        t1 = time()
        ret = self.func(*args)
        dif_time = time() - t1
        print("%s: returned %s in %f seconds" % (self.func.__name__, ret, dif_time))
        return ret


def comp(f1, f2, *args):
    t1 = time()
    r1 = f1(*args) if f1 is not None else None
    t2 = time()
    r2 = f2(*args) if f2 is not None else None
    t3 = time()
    res = "%5s: %s in %f\n%5s: %s in %f" % (f1.__name__ if f1 is not None else None, r1, t2 - t1,
                                            f2.__name__ if f2 is not None else None, r2, t3 - t2)
    if r1 != r2:
        dr = "!! DIFFERENT RESULTS !!"
        res = dr + "\n" + res + "\n" + dr
    print(res)
    return r1 if r1 == r2 else None

# decorator to memoized a function
class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

def mul2(a, b):
    m = {"1":
             {"1": "1", "i": "i", "j": "j", "k": "k"},
         "i":
             {"1": "i", "i": "-1", "j": "k", "k": "-j"},
         "j":
             {"1": "j", "i": "-k", "j": "-1", "k": "i"},
         "k":
             {"1": "k", "i": "j", "j": "-i", "k": "-1"}}

    sign = 0
    if a[0] == "-":
        a = a[1]
        sign += 1
    if b[0] == "-":
        b = b[1]
        sign += 1
    r = m[a][b]
    if r[0] == '-':
        sign += 1
        r = r[1]
    if sign % 2 == 1:
        r = "-%s" % r
    return r


m = {"1":
         {"1": "1", "i": "i", "j": "j", "k": "k", "-1": "-1", "-i": "-i", "-j": "-j", "-k": "-k"},
     "i":
         {"1": "i", "i": "-1", "j": "k", "k": "-j", "-1": "-i", "-i": "1", "-j": "-k", "-k": "j"},
     "j":
         {"1": "j", "i": "-k", "j": "-1", "k": "i", "-1": "-j", "-i": "k", "-j": "1", "-k": "-i"},
     "k":
         {"1": "k", "i": "j", "j": "-i", "k": "-1", "-1": "-k", "-i": "-j", "-j": "i", "-k": "1"},
     "-1":
         {"1": "-1", "i": "-i", "j": "-j", "k": "-k", "-1": "1", "-i": "i", "-j": "j", "-k": "k"},
     "-i":
         {"1": "-i", "i": "1", "j": "-k", "k": "j", "-1": "i", "-i": "-1", "-j": "k", "-k": "-j"},
     "-j":
         {"1": "-j", "i": "k", "j": "1", "k": "-i", "-1": "j", "-i": "-k", "-j": "-1", "-k": "i"},
     "-k":
         {"1": "-k", "i": "-j", "j": "i", "k": "1", "-1": "k", "-i": "j", "-j": "-i", "-k": "-1"}}

def mul(a, b):

    return m[a][b]
    #if r != mul2(a, b):
    #    print(r, mul2(a, b), a, b)


def multi_mul(s):
    a = "1"
    for i in s:
        a = mul(a, i)
    #print_var("s", "a")
    return a

def alg2(L, X, s):
    final_s = s * X
    for first_split in range(len(final_s) - 2):
        first_part = final_s[:first_split + 1]
        #dbg("testing first_split at %s" % first_split)
        if multi_mul(first_part) != "i":
            continue

        for second_split in range(first_split + 1, len(final_s) - 1):
            #dbg("testing second_split at %s" % second_split)
            second_part = final_s[first_split + 1:second_split + 1]
            if multi_mul(second_part) != "j":
                continue

            third_part = final_s[second_split + 1:]
            if multi_mul(third_part) == "k":
                return "YES"

    #for c in "1ijk":
    #    for d in "1ijk":
    #        print("%sx%s=%s" % (c, d, mul(c, "-" + d)))
    return "NO"

def exp(a, e):
    if a[0] == "-":
        sign = 1
        a = a[1]
    else:
        sign = 0

    if a == "1":
        m = "1"
    else:
        mod_4 = e % 4
        if mod_4 == 0:
            m = "1"
        elif mod_4 == 1:
            m = a
        elif mod_4 == 2:
            m = "-1"
        elif mod_4 == 3:
            m = "-" + a

    if sign == 1 and e % 2 == 1:
        if m[0] == "-":
            return m[1]
        else:
            return "-" + m
    else:
        return m

def exp2(a, e):
    if a[0] == "-":
        sign = 1
        a = a[1]
    else:
        sign = 0
    m = multi_mul(a * e)
    if sign == 1 and e % 2 == 1:
        if m[0] == "-":
            return m[1]
        else:
            return "-" + m
    else:
        return m

def alg(L, X, s):
    final_s = s * X
    s_mul = multi_mul(s)
    first_part = "1"
    first_split = 0
    while first_split < len(final_s) - 2:
        first_part = mul(first_part, final_s[first_split])

        first_split += 1

        #dbg("testing first_split at %s" % first_split)
        if first_part != "i":
            continue

        second_part = "1"
        second_split = first_split  # no + 1, already done on first_split
        while second_split < len(final_s) - 1:
            second_part = mul(second_part, final_s[second_split])
            #assert second_part == multi_mul(final_s[first_split + 1:second_split + 1])

            second_split += 1

            if second_part != "j":
                continue

            i_from_s = second_split % len(s)
            if i_from_s != 0:
                i_next_full_s = second_split + (len(s) - i_from_s)
                third_part_up_to_full_s = multi_mul(final_s[second_split:i_next_full_s])
            else:
                i_next_full_s = second_split
                third_part_up_to_full_s = "1"
            remaining_s = (len(final_s) - i_next_full_s) // len(s)
            third_part = mul(third_part_up_to_full_s, exp(s_mul, remaining_s))

            if third_part == "k":
                dbg("YES %d %d" % (first_split, second_split))
                return "YES"

    #for c in "1ijk":
    #    for d in "1ijk":
    #        print("%sx%s=%s" % (c, d, mul(c, "-" + d)))
    return "NO"


def main():

    #for c in "1ijk":
    #    for i in range(20):
    #        dbg("exp(%s, %s) == %s %s" % (c, i, exp("-" + c, i), exp2("-" + c, i)))
    #        comp(exp, exp2, "-" + c, i)

    #import cProfile
    #cProfile.runctx('alg()', globals(), locals())
    #data = sys.stdin
    data = open("in") # todo
    nb = int(data.readline())
    #a, b = map(int,data.readline().split())
    for icase in range(nb):
        L, X = list(map(int, data.readline().split()))  # int
        #L = list(map(float, data.readline().split()))  # float
        #L = data.readline().split()  # string
        s = data.readline().strip()
        #i = int(data.readline().strip())
        #res = comp(alg, alg2, L, X, s)
        # res = alg(L, X, s)
        res = alg(L, X, s)
        ret = "Case #%d: %s" %(icase + 1, res)
        if print_realtime:
            dbg(ret)
        print(ret)


if __name__ == "__main__":
    main()
