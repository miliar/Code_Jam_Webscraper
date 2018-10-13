from sys import *
from itertools import *

def ilog(x):
    n = 0
    while x > 0:
        x //= 2
        n += 1
    return n

def isqrt(x):
    n = int(x)
    a, b = divmod(ilog(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def palindroms():
    k = 0
    for i in xrange(1, 10):
        yield i
    while True:
        for i in range(10**k, 10**(k+1)):
            yield int(str(i) + str(i)[::-1])
        for i in range(10**k, 10**(k+1)):
            for j in range(10):
                yield int(str(i) + str(j) + str(i)[::-1])
        k += 1

def isPalindrom(n): return str(n) == str(n)[::-1]
def between(a, b, iterable): return takewhile(lambda x: x<b, dropwhile(lambda x: x<a, iterable))
def nbr(iterable): return reduce(lambda x,y: x+1, iterable, 0)

size = int(stdin.readline())

for case in range(1, size+1):
    [a, b] = map(int, stdin.readline().split(' '))
    ra, rb = isqrt(a), isqrt(b)+1
    res = nbr(between(a, b+1, ifilter(isPalindrom, imap(lambda x: x**2, between(ra, rb, palindroms())))))
    print 'Case #%d: %d' % (case, res)
