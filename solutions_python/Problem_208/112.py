from __future__ import division
from functools import wraps
from fileinput import input


memo = {}
def cache(wrapped):


    @wraps(wrapped)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        ret = wrapped(*args)
        memo[args] = ret
        return ret
    return wrapper


@cache
def solver(n, u, v):
    if u == v:
        return 0
    this_hours = horses[u]
    times = []
    cur_dist = lengths[u]
    cur_city = u + 1
    while cur_dist <= this_hours[0]:
        res = solver(n, cur_city, v)
        if not res == -1:
            times.append(res + cur_dist/this_hours[1])
        if cur_city < v:
            cur_dist += lengths[cur_city]
            cur_city += 1
        else:
            break
    if len(times) == 0:
        return -1
    return min(times)

inp = input()

t = int(inp.readline())
for casenr in xrange(1, t+1):
    memo = {}
    n, q = map(int, inp.readline().split())
    horses = [-1]
    for _ in xrange(n):
        horses.append(map(int, inp.readline().split()))
    lengths = [-1]
    for i in xrange(n):
        line = map(int, inp.readline().split())
        if i < n-1:
            lengths.append(line[i+1])
    assert q == 1
    u, v = map(int, inp.readline().split())
    assert u == 1
    assert v == n
    print "Case #{}: {}".format(casenr, solver(n, u, v))

