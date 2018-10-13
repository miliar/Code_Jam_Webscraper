#!/usr/bin/env python

import sys
from functools import wraps

def line():
    return sys.stdin.readline().rstrip("\r\n")

States = tuple((x,y) for x in range(3) for y in range(3))

def tcase():
    n, A, B, C, D, x0, y0, M = map(int, line().split())
    def points():
        x, y = x0, y0
        for i in range(n):
            yield (x, y)
            x = (A*x + B) % M
            y = (C*y + D) % M
    m = dict([((x,y), 0) for x, y in States])
    #print list(points())
    for x, y in points():
        m[(x%3, y%3)] += 1
    #print m
    return compute(m)

def withcases_1arg(cases):
    def decorator(f):
        def test(arg, result):
            assert f(arg) == result
        @wraps(f)
        def wrapper():
            for arg, result in cases:
                yield test, arg, result
        return wrapper
    return decorator

@withcases_1arg([
    ({(0,1): 1, (2,1): 1, (2,2): 1, (1,0): 1}, 1),
    ({(1,2): 1, (2,1): 1, (1,1): 1, (2,0): 1, (2,2): 1, (1,0): 1}, 2),
    ({(0,0): 1}, 0),
    ({(0,0): 3}, 1),
    ({(0,0): 4}, 4),
    ({(0,0): 1, (0,1): 2}, 0),
    ({(0,0): 1, (0,1): 1, (1,2): 1}, 0),
    ({(0,0): 1, (0,1): 1, (0,2): 1}, 1),
    ({(0,0): 1, (0,1): 1, (0,2): 2}, 2),
    ({(0,0): 1, (0,1): 2, (0,2): 2}, 4),
    ({(0,0): 1, (0,1): 2, (0,2): 3}, 7),
])
def test_1(m):
    m = m.copy()
    for p in States:
        m.setdefault(p, 0)
    return compute(m)


def compute(m):
    count = 0
    for x1, y1 in States:
        for x2, y2 in States:
            x3, y3 = ((6-x1-x2)%3, (6-y1-y2)%3)
            count += m[(x1,y1)] * m[(x2,y2)] * m[(x3,y3)]
    for x, y in States:
        count -= m[(x,y)]
    assert count % 6 == 0, count
    count /= 6
    for x, y in States:
        count -= m[(x,y)]*(m[(x,y)]-1) / 2
    return count


def main():
    n_cases = int(line())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %d" % (t_case, tcase())

if __name__ == "__main__":
    main()

# vim: ts=4 sw=4 et
