#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os
import math
import binascii
                            
def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for nt in xrange(ntest):
        l = f.readline().strip().split()  
        if len(l) !=  1:
            print "Error got ", l
            sys.exit(1)

        nteam = int(l[0])
        res = []
        for i in xrange(nteam):
            l = f.readline().strip().split()  
            if len(l) !=  1 and len(l[0]) != nteam:
                print "Error got team", l
                sys.exit(1)
            res.extend(l)

        wp = []
        wins = []
        losses = []
        for i in xrange(nteam):
            win = float(res[i].count( "1" ))
            loss = float(res[i].count( "0" ))
            wins.append( win )
            losses.append( loss )
            wp.append(win / (win + loss))

        owp = []
        for i in xrange(nteam):
            tl = []
            for j in xrange(nteam):
               if res[i][j] == "1":
                    tl.append( wins[j] / (wins[j] + losses[j] - 1.0 ) )
               elif res[i][j] == "0":
                    tl.append( (wins[j] - 1.0) / (wins[j] + losses[j] - 1.0 ) )
                     
            owp.append( sum( tl, 0.0 ) / len(tl) )    

        oowp = []
        for i in xrange(nteam):
            tl = []
            for j in xrange(nteam):
               if res[i][j] == "1" or res[i][j] == "0":
                    tl.append( owp[j] )

            oowp.append( sum( tl, 0.0 ) / len(tl) )    


        print "Case #%d:" % (nt + 1)
        for i in xrange(nteam):
            print (0.25 * wp[i])  +  (0.50 * owp[i]) + ( 0.25 * oowp[i])


if __name__ == "__main__":
    main()

