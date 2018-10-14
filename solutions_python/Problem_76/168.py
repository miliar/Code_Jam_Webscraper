#!/usr/bin/env python

import fileinput

lines = fileinput.input()

def foo():
    i = iter(fileinput.input())
    i.next()
    while True:
        i.next()
        yield i.next().rstrip()

for i, candy in enumerate(foo()):
    candy = map(int, candy.split())
    xor = 0
    for c in candy:
        xor = xor ^ c
    if xor != 0:
        res = 'NO'
    else:
        res = sum(candy) - min(candy)
    print "Case #%d: %s" % (i+1, res)
