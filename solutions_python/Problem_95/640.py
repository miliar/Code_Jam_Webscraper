#!/usr/bin/env python2

f = open('i', 'r')

n = int(f.readline()[:-1])

m = {}
m[' '] = ' '
m['a'] = 'y'
m['b'] = 'h'
m['c'] = 'e'
m['d'] = 's'
m['e'] = 'o'
m['f'] = 'c'
m['g'] = 'v'
m['h'] = 'x'
m['i'] = 'd'
m['j'] = 'u'
m['k'] = 'i'
m['l'] = 'g'
m['m'] = 'l'
m['n'] = 'b'
m['o'] = 'k'
m['p'] = 'r'
m['q'] = 'z'
m['r'] = 't'
m['s'] = 'n'
m['t'] = 'w'
m['u'] = 'j'
m['v'] = 'p'
m['w'] = 'f'
m['x'] = 'm'
m['y'] = 'a'
m['z'] = 'q'


for i in range(n):
    s = f.readline()[:-1]
    ss = ''
    for j in range(len(s)):
        ss += m[s[j]]
    print 'Case #%d: %s' % (i+1, ss)
