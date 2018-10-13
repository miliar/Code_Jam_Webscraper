#!/usr/bin/env python

import os, sys
import codejam
import fractions

def hotdogs(testcase):
    testdata = [int(x) for x in testcase[0].split(" ")]
    if len(testcase) < 2 or len(testdata) != 2 or len(testcase) != 1+testdata[0]:
        raise RuntimeError, "Oops, we got a bad testcase!"
    nspots = testdata[0]
    distance = testdata[1]
    spots = []
    movetime = 0
    earliestmove = None
    lastorigspot = fractions.Fraction(-999999999, 1)
    lastrightspot = fractions.Fraction(-999999999, 1)
    lastspotnum = 0
    for i in range(nspots):
        testdata = [int(x) for x in testcase[i+1].split(" ")]
        if len(testdata) != 2:
            raise RuntimeError, "Oops, we got a bad testline!"
        spot = testdata[0]
        ncarts = testdata[1]
        spots.append( (spot, ncarts) )
        spotstretch = (ncarts-1) * distance
        spotplus = fractions.Fraction(spot*2+spotstretch, 2)
        earliestspottomoveto = fractions.Fraction(spot*2-spotstretch, 2)
        #print "Considering spot %d, carts %d (distance %d, lastright %g)..." % (spot, ncarts, distance, lastrightspot)
        if earliestspottomoveto < lastrightspot + distance:
            # We need to include the last set of spots in this.
            numtostretch = ncarts+lastspotnum
            newtotalstretch = (numtostretch-1)*distance
            oldtotalstretch = spot - lastorigspot
            lastrightspot = fractions.Fraction(spot*2+newtotalstretch-oldtotalstretch, 2)
            lastspotnum = numtostretch
            spotstretch = fractions.Fraction(newtotalstretch-oldtotalstretch, 2)
            #print " combining with last set, setting numtostretch to %d, newtotalstretch to %d, oldtotalstretch to %d, lastright to %g, lastspotnum to %d, stretch to %g" % (numtostretch, newtotalstretch, oldtotalstretch, lastrightspot, lastspotnum, spotstretch)
            if spotstretch > movetime:
                #print " and setting move time to %g" % spotstretch
                movetime = spotstretch
        else:
            # We can stretch out just fine.
            lastorigspot = spot
            lastrightspot = spotplus
            lastspotnum = ncarts                                                                                     
            spotstretch = fractions.Fraction(spotstretch, 2)
            #print " working solo, setting lastright to %g, lastspotnum to %d, stretch to %g" % (lastrightspot, lastspotnum, spotstretch)
            if spotstretch > movetime:
                #print " and setting move time to %g" % spotstretch
                movetime = spotstretch
            
    return ("%15.6g" % movetime).strip()

def extra_lines(lines):
    data = [int(x) for x in lines[0].split(" ")]
    return data[0]

if __name__ == "__main__":
    codejam.main(sys.argv[1:], hotdogs, 1, extra_lines=extra_lines)
