import sys,math

T = int(sys.stdin.readline())
for i in range(1,T+1):
    line = sys.stdin.readline()
    r, rem = [int(x) for x in line.split()]
    tot = 0
    r+=1
    while rem >= 0:
        con = (r*r)-(r-1)**2
        rem = rem - con
        #print "t={0}".format(con)
        r += 2
        if (rem >= 0):
            tot = tot+1
    print "Case #{0}: {1}".format(i,tot)