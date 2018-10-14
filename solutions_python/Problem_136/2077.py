__author__ = 'Pravesh'

import sys


file = open("in.in","r")

sys.stdout = open("out","w")

for i in range(int(file.readline())):
    C, F, X = (float(x) for x in file.readline().split())
    #C, F, X = 500., 4., 2000.
    index = 0
    R = 0
    t = 0

    r = lambda x: 2+x*F
    while True:
        if X/r(index) < X/(r(index+1)) + C/r(index):
            t = R + X/(r(index))
            break
        R += C/r(index)
        index += 1


    print "Case #%d: %.7f" % (i+1, t)