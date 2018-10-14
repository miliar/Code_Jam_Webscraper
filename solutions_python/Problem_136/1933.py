#!/usr/bin/env python

from sys import argv

ansStr = "Case #%d: %.7f"
out = []
with open(argv[1]) as infile:
    nCases = int(infile.next())
    for n in xrange(nCases):
        c, f, x = map(float, infile.next().split())
        # compute best strat
        i = 0
        lastTime = 0.0
        while True:
            j=0
            time=0.0
            while j<i:
                time += c/(2.0+j*f)
                j += 1
            time += x/(2.0+j*f)
            if time < lastTime or lastTime==0.0:
                lastTime = time
            else:
                break
            i += 1          
        out.append(ansStr % (n+1, lastTime))
        
with open('cookie_clicker.out', 'w') as outf:
    for s in out:
        outf.write(s + "\n")
        
    
        
    
