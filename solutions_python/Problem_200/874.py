def digits(x):
    return [ int(c) for c in str(x) ]

def of_digits(ds):
    s = 0
    for d in ds:
        s *= 10
        s += d
    return s

def is_tidy(N):
    ds = digits(N)
    max_ = 0
    for d in ds:
        if d >= max_:
            max_ = max(max_, d)
        else:
            return False
    return True

def biggest_tidy(N):
    if not is_tidy(N):
        ds = digits(N)
        left = of_digits(ds[:-1]) - 1
        return of_digits(digits(biggest_tidy(left)) + [9])
    else:
        return N
        
def case(N):
    print "N:", N
    ds = digits(N)
    num_digits = len(ds)
    print "digits:", ds
    print "is tidy:", is_tidy(N)
    r = biggest_tidy(N)
    print "biggest tidy:", r
    return r

import fileinput
stdin = fileinput.input()
T = int(next(stdin))
print "T:", T

for n in range(1, T+1):
    N = int(next(stdin))
    tidy = case(N)
    print "Case #{}: {}".format(n, tidy)
