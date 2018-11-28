#!/usr/bin/env python
import sys
from copy import copy

def memoize(fn):
    map = {}
    def f(*args):
        try:
            return map[args]
        except KeyError:
            map[args] = x = fn(*args)
            return x
    return f

def read(name="input"):
    name = sys.argv[1] if len(sys.argv) > 1 else name
    return [line.strip() for line in open(name).readlines()]

@memoize
def foo(sw, current, es, qs):
    if not qs:
        return sw
    if current == qs[0]:
        return min(foo(sw + 1, e, es, qs) for e in es if e != current)
    else:
        return foo(sw, current, es, qs[1:])

def bla(es, qs):
    return min(foo(0, e, es, qs) for e in es)

def main():
    input = read()
    cases = int(input.pop(0))
    for case in range(cases):
        print "Case #%d: " % (case + 1),
        s = int(input.pop(0))
        engines, input = input[:s], input[s:]
        q = int(input.pop(0))
        queries, input = input[:q], input[q:]
        print bla(*[tuple(x) for x in engines, queries])
        

if __name__ == '__main__':
    main()
