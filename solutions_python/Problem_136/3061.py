__author__ = 'mfranzen'
__input__ = 'B-large.in'
__output__ = 'B-large.out'

import math

# read input
f = open(__input__, 'r')

# read number of instances
T = int(f.readline().strip())

for t in range(T):
    C, F, X = [float(x) for x in f.readline().strip().split(' ')]

    #b = 0
    #while (X / (2 + b*F)) > (C / (2 + b*F)) + (X / (2 + (b+1)*F)):
    #    b += 1

    b = math.ceil((F*X/C - 2)/F - 1)
    out = 0.0
    if b > 0:
        for a in range(b):
            out += C / (2 + a*F)
        out += X / (2 + b*F)
    else:
        out += X / 2
    s = "Case #%d: %f\n" % (t+1, out)
    with open(__output__, 'a') as o:
        o.write(s)