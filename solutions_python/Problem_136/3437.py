#/usr/bin/python2.7

import sys

fname = sys.argv[1]

#C=500.0, F=4.0 and X=2000.0
count = 0
c = 0
f = 0
x = 0
dcount = 0 
mtime = 0

def do(case, t):
    c = float(t[0]) # the count of cookies now // start with 0
    f = float(t[1]) # farm's earn
    x = float(t[2]) # required the count of cookies
#    print "c"
#    print c
#    print "f"
#    print f
#    print "x"
#    print x
    s = 2 # cookie per second
    fc = 0 # farm count
    acf = [1, 0]
    while (acf[0] > acf[1]):
#    while (p1 != True and p2 != True):
        
        base = [0] + [1/(s + f*(i)) for i in range(0, fc+1)]
        acf = [(c * sum(base[0:i+1]) + x/(s+((i)*f))) for i in range(fc, fc+2)]
#        print acf
        fc += 1
    print "Case #%s: %.7f" % (case, acf[0])
#        print "base"
#        print base
#        print "acf"
#        print acf
#        break #exit(0)
#        acf0 = c()




with open(fname) as f:
    for line in f:
        if (count == 0):
            count = int(line)
#            print "Count of Tests: %s" % count
            continue

        test = (line.split("\n")[0]).split(" ")
        dcount += 1
        do(dcount, test)





