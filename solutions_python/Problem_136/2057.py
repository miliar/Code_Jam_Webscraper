from __future__ import division

'''
some math approaches were used
'''

tc = input()
for tid in range(1, tc + 1):
    line = raw_input()
    C, F, X = map(float, line.split())
    if C >= X:
        k = 0
    elif X * F < 2.0 * C:
        k = 0
    else:
        k = int((X * F - 2 * C) / (F * C))
    Tk = X / (k * F + 2)
    for i in range(k):
        Tk += C / (2 + i * F)
    Tk = "%.7f" % Tk
    print "Case #" + str(tid) + ": " + Tk

