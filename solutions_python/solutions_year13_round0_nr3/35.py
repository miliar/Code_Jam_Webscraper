#!/usr/bin/python

from bisect import bisect, bisect_left
from sys import argv

limit = 10**50+1
if len(argv) == 2:
    limit = int(argv[1]) + 1

numbers = set([1,4,9])

def gen(now, ds):
    #print now

    def check(num, ds):
        if num > limit or ds >= 10:
            return
        numbers.add(num*num)

    s = str(now)
    r = s[::-1]
    nds = ds * 2
    if nds >= 10 or int(s+r) > limit:
        return

    check(int(s + r), nds)
    check(int(s + '0' + r), nds)
    check(int(s + '1' + r), nds + 1)
    check(int(s + '2' + r), nds + 4)

    gen(now * 10, ds)
    gen(now * 10 + 1, ds + 1)

gen(1, 1)
gen(2, 4)
fairs = sorted(numbers)
#print fairs

def get():
    a, b = map(int, raw_input().strip().split())
    return bisect(fairs, b) - bisect_left(fairs, a)

n = input()
for x in xrange(n):
    print 'Case #%d: %s' % (x+1, get())
