'''
Created on Apr 14, 2012

@author: herman
'''

from string import split

infile = open("large_input.txt","r")
outfile = open("large_output.txt","w")

trials = int(infile.readline())

for i in xrange(trials):
    vals = [int(x) for x in infile.readline().split()]
    N = vals[0]
    S = vals[1]
    p = vals[2]
    tpoints = vals[3:]
    
    # min num surprises used
    nsur = 0
    # max googlers b >= p
    maxbest = 0
    
    for t in tpoints:
        base = t/3
        mval = t % 3
        if mval == 0:
            # no choice here
            if p <= base:
                maxbest += 1
            if base != 0 and base != 10:
                if p == base + 1 and nsur < S:
                    maxbest += 1
                    nsur += 1
        elif mval == 1:
            if p <= base + 1:
                maxbest += 1
        else:
            if p <= base + 1:
                maxbest += 1
            if base != 9:
                if p == base + 2 and nsur < S:
                    maxbest += 1
                    nsur += 1

    str = "Case #%d: %d\n" % ((i+1),maxbest)
    print str
    outfile.write(str)

infile.close()
outfile.close()