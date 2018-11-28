#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os
import math
import binascii

bl = [ 'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F' ]

def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for nt in xrange(ntest):
        l = f.readline().strip().split()  
        
        ncomb = int(l[0])
        cdict = dict() 
        idx = 0
        for i in xrange(ncomb):
            idx += 1
            cstr = l[idx]
            if len(cstr) != 3:
                print "Error cstr = ", cstr
                sys.exit(1)
            cdict[ "" + cstr[0] + cstr[1] ] = cstr[2]
            cdict[ "" + cstr[1] + cstr[0] ] = cstr[2]


        kdict = dict()
        for i in xrange(len(bl)):
            kdict[ bl[i] ] = set()           

        idx += 1
        nkill = int(l[idx])
        for i in xrange(nkill):
            idx += 1
            cstr = l[idx]
            if len(cstr) != 2:
                print "Error kstr = ", cstr
                sys.exit(1)
            kdict[ cstr[0] ].add( cstr[1] )
            kdict[ cstr[1] ].add( cstr[0] )
        

        idx += 1
        slen = int(l[idx])
        idx += 1
        s = l[idx]
        
        if len(l) != (idx + 1) or len(s) != slen:
            print "Error l = ", l
            sys.exit(1)

        fl = []
        for i in xrange(slen):
            #combine
            combined = False
            if ( len(fl) > 0 ):
                lp = ""
                lp += fl[-1]
                lp += s[i] 
                if lp in cdict:
                    fl[-1] = cdict[lp]
                    combined = True
         
            #kill       
            kill = False
            if not combined:
                kset = kdict[s[i]]
                for j in xrange(len(fl)):
                    if fl[j] in kset:
                        kill = True
                        break
            
            if kill:
                fl = []
            elif not combined:
                fl.append( s[i] )
        
        #print cdict
        #print kdict
        #print s
        fstr = "["
        for i in xrange(len(fl)):
            if i > 0:
                fstr += ", "
            fstr += fl[i]
        fstr += "]"
        
        print "Case #%d: %s" % (nt + 1, fstr)
            

if __name__ == "__main__":
    main()

