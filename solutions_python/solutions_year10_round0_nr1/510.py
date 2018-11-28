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

def snap(snappers):
    s = snappers[:]
    i = 0
    while (i < len(snappers)) and (i == 0 or snappers[i-1] == 1):
        s[i] = (snappers[i] + 1) % 2
        i += 1
    return s

def all_on(snappers):
    for s in snappers:
        if s == 0:
            return False
    return True

def calc2(n, k):
    return (k+1) % (2**n) == 0

def calc(n, k, snappers):
    return calc2(n, k)
    print n, k, snappers, calc2(n, k)
    if k == 0:
        return all_on(snappers)
    else:
        k -= 1
        snappers = snap(snappers)
        return calc(n, k, snappers)


def doit(N, K):
    if calc2(N, K):
        return "ON"
    else:
        return "OFF"

if len(sys.argv) == 1:
    filename = "t.in"
else:
    filename = sys.argv[1]
f = open(filename)
f_out = open(filename[:-2] + "out", "w")
T = int(f.readline())
for i in range(T):
    a = f.readline()
    N, K = a.split()
    s = "Case #%d: %s" % (i+1, doit(int(N), int(K)))
    print s
    f_out.write(s + "\n")
