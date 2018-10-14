#!/usr/bin/env python

if __name__ == '__main__':
    
    t = int(raw_input())
    for case in xrange(1, t+1):
        bact = set()
        r = int(raw_input())
        for a in xrange(r):
            x1, y1, x2, y2 = map(int, raw_input().split(' '))
            for y in xrange(y1, y2+1):
                for x in xrange(x1, x2+1):
                    bact.add((y,x))
        
        result = 0
        while len(bact) > 0:
            new_bact = set()
            for bac in bact:
                if (bac[0]-1, bac[1]) in bact or (bac[0], bac[1]-1) in bact:
                    new_bact.add(bac)
                if (bac[0]+1, bac[1]-1) in bact and bac[0]+1<= 100:
                    new_bact.add((bac[0]+1, bac[1]))
                if (bac[0]-1, bac[1]+1) in bact and bac[1]+1<= 100:
                    new_bact.add((bac[0], bac[1]+1))
            result += 1
            bact = new_bact
        
        print "Case #%d: %d" % (case, result)