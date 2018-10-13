
from sys import argv, setrecursionlimit
import linecache

setrecursionlimit(10000)

filename = argv[1]
num = int(linecache.getline(filename, 1))

def time_to_get_all(r, X):
    return X/r

# How long to get n farms.
def time_to_build(n, C, F):
    t = C / 2.
    f = 1
    r = 2. + F

    while f < n:
        t = t + C / r
        f += 1
        r += F

    return t

for i in range(num):
    C, F, X = map(float, linecache.getline(filename, i+2).strip().split())

    time = time_to_get_all(2., X)
    f = 1

    while(True):
        r = 2. + F*f
        t = time_to_build(f, C, F) + time_to_get_all(r, X)
        
        if t < time:
            time = t
        else:
            break
        f += 1

    print "Case #%i: %.7f" % (i+1, time)
