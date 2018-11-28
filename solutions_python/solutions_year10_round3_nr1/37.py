#!/bin/python

filename = "A-large"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")

T = int(infile.readline())
for case in xrange(T):
    K = 0
    N = int(infile.readline())
    wires = [map(int, infile.readline().split()) for i in xrange(N)]
    
    # Count crossing wires
    for w in xrange(len(wires)):
        a, b = wires[w]
        for w2 in xrange(w+1,len(wires)):
            a2, b2 = wires[w2]
            if (a < a2 and b > b2) or (a > a2 and b < b2):
                K += 1
    
    outfile.write("Case #%d: %d\n" % (case+1, K))

infile.close()
outfile.close()