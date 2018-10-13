import sys, itertools

def isPalindrome(x):
    s = str(x)
    return s == s[::-1]

def genPals():
    sz = 0
    while True:
        sz = sz + 1
        half = (sz + 1) >> 1
        if sz & 1:
            for n in xrange(10**(half-1), 10**half):
                s = str(n)
                yield int(s[:-1:] + s[::-1])
        else:
            for n in xrange(10**(half-1), 10**half):
                s = str(n)
                yield int(s + s[::-1])

def genSquares(seed):
    while True:
        yield next(seed) ** 2

def f(a, b):
    drop = itertools.dropwhile
    take = itertools.takewhile
    g = genSquares(genPals())
    return len(filter(isPalindrome,
            take(lambda x: x <= b, drop(lambda x: x < a, g))))

s = sys.stdin
T = int(s.readline())
for t in range(T):
    sys.stdout.write("Case #{}: {}\n".format(t + 1, f(*map(int,
        s.readline().split()))))
