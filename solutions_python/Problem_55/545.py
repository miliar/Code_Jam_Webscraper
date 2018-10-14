#!/usr/bin/env python

import sys, os
    
def main():
    infile = "C-small-attempt0.in"
    outfile = "C-small.out"
    
    fin = open(infile)
    fout = open(outfile, "w+")
    
    T = int(fin.readline())
    
    for case in range(0,T):
        [R, k, N] = [int(i) for i in fin.readline().split()]
        g = [int(i) for i in fin.readline().split()]
        
        if len(g) != N:
            print ("Error, len(g) != N")
            sys.exit(1)
        
#        print g
        next = []
        m = []
        
        for i in range(0,len(g)):
            sum = 0
            j = i

            while True:
                if (sum + g[j]) > k:
                    next.append(j)
                    m.append(sum)
                    break
                sum += g[j]
                j = (j+1) % N
                
                if j == i:
                    next.append(j)
                    m.append(sum)
                    break
        
#        print "next", next
#        print "m:", m
        
        total = 0
        n = 0
        for i in range(0,R):
            total += m[n]
            n = next[n]
            
        fout.write("Case #%d: %d\n" % (case+1, total))
    
    
if __name__=="__main__":
    main()
