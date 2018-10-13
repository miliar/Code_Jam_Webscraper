#!/usr/bin/python -tt

import sys

def main():
    if len(sys.argv) != 2:
        print 'Requires input file'
        sys.exit()
    fname = sys.argv[1]
    fptr = open(fname, 'r')
    numtest = int(fptr.readline().split(' ')[0])
    outptr = open('output', 'w')
    
    for i in xrange(numtest):
        # Read num teams
        numteams = int(fptr.readline().split(' ')[0])
        # Read grid
        maingrid = [list(fptr.readline().split('\n')[0]) for j in xrange(numteams)]
        #print maingrid
        #print "Played, won"
        WP = []
        Played = []
        for j in xrange(numteams):
            Played.append(numteams - maingrid[j].count("."))
            WP.append(float(maingrid[j].count("1"))/Played[j])
        
        #print Played
        #print WP
        
        OWP = []
        for j in xrange(numteams):
            OWPt = 0
            for k in xrange(numteams):
                if k == j:
                    continue
                if maingrid[k][j] == ".":
                    continue
                numpl = Played[k]
                numwon = maingrid[k].count("1")
                if maingrid[k][j] == "1":
                    numpl = numpl - 1
                    numwon = numwon -1
                elif maingrid[k][j] == "0":
                    numpl = numpl -1
                if numpl == 0:
                    OWPt = OWPt + 0
                else:
                    OWPt = OWPt + (float(numwon)/numpl)
                #print 'OWPt = %f\n'% OWPt
            #print 'OWP = %f\n'% (float(OWPt)/Played[j])
            OWP.append(float(OWPt)/Played[j])
         
        #print "OWPs"   
        #print OWP
        OOWP = []
        for j in xrange(numteams):
            OOWPt = 0
            for k in xrange(numteams):
                if maingrid[j][k] != ".":
                    OOWPt = OOWPt + OWP[k]
            OOWP.append(OOWPt/Played[j])
         
        outptr.write('Case #%d:\n'% (i+1))    
        # Find RPI
        for j in xrange(numteams):
            #print WP[j], OWP[j], OOWP[j]
            outptr.write("%f\n" % ((0.25*WP[j]) + (0.5*OWP[j]) + (0.25*OOWP[j])))

    outptr.close()
    fptr.close()
        

if __name__ == '__main__':
    main()