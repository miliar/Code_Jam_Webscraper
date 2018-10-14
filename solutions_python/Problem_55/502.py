from functools import wraps
import sys

_cache = {}

def cache(func):
    @wraps(func)
    def wrapper(a, w):
        key = (a, w)
        if key in _cache:
            return _cache[key]
        r = func(a, w)
        _cache[key] = r
        return r
    return wrapper

def delete_cache():
    global _cache
    _cache = {}

def ride(k, gi):
    total = 0
    i = 0
    while i < len(gi) and total + gi[i] <= k:
        total += gi[i]
        i += 1
    return total, i

def doit(R, k, gi):
    assert R > 0
    total = 0
    while R > 0:
        _total, i = ride(k, gi)
        total += _total
        gi = gi[i:] + gi[:i]
        R -= 1
        if R == 0:
            return total

if len(sys.argv) == 1:
    filename = "t.in"
else:
    filename = sys.argv[1]
f = open(filename)
f_out = open(filename[:-2] + "out", "w")
T = int(f.readline())
for i in range(T):
    R, k, N = [int(x) for x in f.readline().split()]
    gi = [int(x) for x in f.readline().split()]
    assert len(gi) == N
    s = "Case #%d: %s" % (i+1, doit(R, k, gi))
    print s
    f_out.write(s + "\n")
