#!/usr/bin/env python

import multiprocessing
import functools
import itertools as it
import sys

#from ipdb import launch_ipdb_on_exception

#import gc


def _memo(func, keynames=None):
    """
    apply dynamic programming to func
    """
    cache = {}
    code = func.func_code
    if not keynames:
        keynames = code.co_varnames

    def key(args, kwargs):
        """
        Construct a tuple of relevant arg values
        """
        named_args = dict(zip(code.co_varnames, args))
        named_args.update(kwargs)
        ndefaults = len(func.func_defaults or [])
        named_args.update(zip(code.co_varnames[code.co_argcount - ndefaults:],
                              (func.func_defaults or [])))
        return tuple(named_args[arg] for arg in keynames)

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        "lookup the args to see if an answer has been computed previously"
        call_key = key(args, kwargs)
        if call_key not in cache:
            cache[call_key] = func(*args, **kwargs)
        return cache[call_key]

    wrapped.cache = cache

    return wrapped


def memo(*varnames):
    """
    memoise a function using a subset of its named arguments
    """
    if not varnames:
        varnames = None
    return lambda f: _memo(f, varnames)


def parse(*args):
    default = args[-1] if args else int
    return [ctor(x)
            for ctor, x in it.izip(args + (default,)*10000,
                                   raw_input().strip().split())]


class TestCase(object):
    """
    Template for solving test cases
    """

    def __init__(self, idx):
        self.idx = idx
        # parse input
        inp = raw_input().strip().split()
        self.initargs = (inp[0], int(inp[1]))
        self.cache = {}

    def _solve(self, string, nseq, start=0):
        """
        return no of consecutive constanants right of start
        """
        if start not in self.cache:
            if start > len(string) - nseq:
                self.cache[start] = 0
            elif not any(ch in 'aeiou' for ch in string[start:start+nseq]):
                self.cache[start] = len(string) - nseq - start + 1
            else:
                self.cache[start] = self._solve(string, nseq, start + 1)
        return self.cache[start]

    def solve(self, string, nseq):
        ## print [(string[i:], self._solve(string, nseq, i))
        ##            for i in xrange(len(string) - nseq + 1)]
        return sum(self._solve(string, nseq, i)
                   for i in xrange(len(string) - nseq + 1))

    @property
    def result(self):
        """
        IMPLEMENT ME
        """
        #with launch_ipdb_on_exception():
        return self.solve(*self.initargs)

    def __str__(self):
        return 'Case #{self.idx}: {self.result}'.format(self=self)


def main(argv):
    """
    parse and (possible concurrently) run all test cases
    """
    solvers = []
    ncases = int(raw_input())

    for i in xrange(ncases):
        solvers.append(TestCase(i+1))

    if 'conc' in argv:
        pool = multiprocessing.Pool(2)
    else:
        pool = it

    sys.setrecursionlimit(20000)

    for soln in pool.imap(str, solvers):
        print soln
    if 'conc' in argv:
        pool.close()
        pool.join()


if __name__ == '__main__':
    main(sys.argv)
