
import sys
import itertools
import functools

f = 2

@functools.lru_cache(maxsize=None)
def get_farm_duration(C, F, X, N):
    d = 0
    for n in range(N):
        d += C / (f + n * F)
    return d

def get_duration(C, F, X, N):
    return get_farm_duration(C, F, X, N) + X / (f + N * F)

with open('in.txt') as fp:
    T = int(fp.readline())
    for t in range(1, T + 1):
        C, F, X = map(float, fp.readline().split(' '))

        # print(C, F, X)

        d = sys.float_info.max

        for n in itertools.count(0):
            d_a = get_duration(C, F, X, n)
            if d_a >= d:
                break
            d = d_a
        print("Case #%d: %0.7f" % (t, d, ))

