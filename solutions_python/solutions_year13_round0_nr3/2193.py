from math import sqrt
from itertools import permutations
import gmpy

n = int(raw_input().strip())
terminal = range(1, 10)
middle = range(10)

def check(p, interval):
    return p >= interval[0] and p <= interval[1]

def is_it(a):
    if str(a) == str(a)[::-1]:
        if gmpy.is_square(a):
            s = gmpy.sqrt(a)
            if str(s) == str(s)[::-1]:
                return True
tc = 1
while tc <= n:
    nos = 0
    interval = raw_input().strip().split(" ")
    interval = [int(a) for a in interval]
    a = 0
    l1 = len(str(interval[0]))
    l2 = len(str(interval[1]))
    palin = interval[0]
    for d in range(l1, l2 + 1):
        if d == 1:
            for m in range(interval[0], 10):
                if m > interval[1]:
                    break
                if is_it(m):
                    nos += 1
        else:
            for x in range(1, 10):
                for ys in permutations(range(10), d/2 - 1):
                    for z in (range(10) if d % 2 else (None, )):
                        a = int(''.join(map(str, (([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if d%2
                                                  else ([x]+list(ys)+list(ys)[::-1]+[x])))))
                        if check(a, interval):
                            if is_it(a):
                                nos += 1

    print "Case #%d: %d" % (tc, nos,)
    tc += 1
