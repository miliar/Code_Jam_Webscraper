#/usr/bin/env python

def solve(c, f, x):
    a = 2.0
    t = 0.0
    while 1:
        if (x / a) > (c / a):
            t += (c / a)
            x -= c
            if ((x+c) / (a+f)) < ((x) / a):
                # should buy
                x += c
                a += f
        else:
            return (t + (x / a))

N = int(raw_input())
for i in range(N):
    L = raw_input()
    V = L.split()
    C = float(V[0])
    F = float(V[1])
    X = float(V[2])
    print 'Case #' + str(i+1) + ': ' + "%.7f" % solve(C, F, X)
