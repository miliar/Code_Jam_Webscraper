import sys

from pprint import pprint

t = int(raw_input())

old_ttf = {}

def ttf(c, f, nb_f):
    if nb_f == 0:
        return 0.0

    key = ','.join([str(c), str(f), str(nb_f)])

    if key not in old_ttf:
        old_ttf[key] = (c / (2 + float(nb_f - 1) * f)) + ttf(c, f, nb_f - 1)
    return old_ttf[key]

def ttt(c, f, x, nb_f):
    return (x / (2.0 + f * float(nb_f))) + ttf(c, f, nb_f)

def time(c, f, x):
    nb_f = 0
    t = ttt(c, f, x, nb_f)
    while True:
        nb_f += 1
        new_t = ttt(c, f, x, nb_f)
        if t < new_t:
            return t
        t = new_t

for i in xrange(t):
    old_ttf = {}
    d = raw_input().split()
    c = float(d[0])
    f = float(d[1])
    x = float(d[2])
    print 'Case #%i: %0.7f' % (i + 1, time(c, f, x))