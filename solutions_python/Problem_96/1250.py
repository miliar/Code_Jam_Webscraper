#!/usr/bin/python

f = file('q2.in', 'r')

# What is the minimal max score if it is unsurprising?
def m(t):
    return ((t - 1) / 3) + 1

def dance(N, S, p, t):
    max_scores = [m(ti) for ti in t]
    if p == 0:
        return N
    if p == 1:
        return len([1 for s in max_scores if s > 0])
    return len([1 for s in max_scores if s >= p]) + min(S, len([1 for s in max_scores if s == p - 1]))

i = 0
for l in f:
    if i > 0:
        l = [int(n) for n in l.split(" ")]
        N = l[0]
        S = l[1]
        p = l[2]
        t = l[3:]
        print ("Case #%d: %d" % (i, dance(N, S, p, t)))
    i = i + 1
f.close()
