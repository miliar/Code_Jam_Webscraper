import sys

__author__ = 'dkopiychenko'

import os

def multiply(x, y):
    if x == '1': return 1, y
    if y == '1': return 1, x
    if x == 'i':
        if y == 'i': return -1, '1'
        if y == 'j': return 1, 'k'
        if y == 'k': return -1, 'j'
    if x == 'j':
        if y == 'i': return -1, 'k'
        if y == 'j': return -1, '1'
        if y == 'k': return 1, 'i'
    if x == 'k':
        if y == 'i': return 1, 'j'
        if y == 'j': return -1, 'i'
        if y == 'k': return -1, '1'

def g(sign, s, p):
    if s[0] == p: return sign, s[1:]
    if len(s) < 2: return None
    sign2, ss = multiply(s[0], s[1])
    return g(sign*sign2, ss+s[2:], p)

def g1(sign, s):
    if len(s) == 0: return sign == 1
    if len(s) == 1: return (s[0] == '1' and sign == 1)
    sign2, ss = multiply(s[0], s[1])
    return g1(sign*sign2, ss+s[2:])

def check(s):
    # print s
    a = g(1, s, 'i')
    if a == None: return 'NO'
    b = g(a[0], a[1], 'j')
    if b == None: return 'NO'
    c = g(b[0], b[1], 'k')
    if c == None: return 'NO'
    if not g1(c[0], c[1]): return 'NO'
    return 'YES'

sys.setrecursionlimit(20000)

with open(os.path.expanduser("~/gcj2015/input03s.txt")) as f:
    n = int(f.readline().strip('\n'))
    print n
    lines = [x.strip('\n') for x in f.readlines()]
    counter = 1
    for i in range(n):
        l,x = lines[2*i].split(' ')
        s = lines[2*i + 1]
        ss = ''
        for i in range(int(x)):
            ss += s
        print 'Case #' + str(counter) + ': ' + check(ss)
        counter += 1


