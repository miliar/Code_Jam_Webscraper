from __future__ import division
from fractions import Fraction
from math import ceil

root = r"C:/Python27/Mine/codejam/"

def solve(fname,outname = "D-small.out"):
    infile = open(root + fname,'rU')
    outfile = open(root + outname,'w')
    return solve_inner(infile,outfile)

def solve_inner(infile,outfile):
    casesline = infile.readline()
    cases = int(casesline)
    for case in xrange(1,cases + 1):
        instructionsline = infile.readline()
        instructionset = instructionsline.strip().split(" ")
        args = [int(ci) for ci in instructionset]
        if case > 1:
            outfile.write("\n")
        outfile.write("Case #%s: %s" % (case,processCase(args)))
    return True

def processCase(args):
    N, PD, PG = args
    return "Possible" if freecell(N,PD,PG) else "Broken"

def freecell(N,PD,PG):
    dFrac = Fraction(PD,100)
    dMin = dFrac.denominator
    dSteps = N//dMin
    if dSteps <= 0: #note that Fraction(0,100) becomes Fraction(0,1)
        return False
    if (PG <= 0 and PD > 0) or (PG >= 100 and PD < 100):
        return False #whoops, no wins possible
    return True

##def freecell(N,PD,PG):
##    dFrac = Fraction(PD,100)
##    dMin = dFrac.denominator
##    pdMin = dFrac.numerator
##    dSteps = N//dMin
##    if dSteps <= 0: #note that Fraction(0,100) becomes Fraction(0,1)
##        print dFrac, pdMin, dMin, dSteps
##        return False
##    dMax = dSteps*dMin
##    pdMax = dSteps*pdMin
##    gFrac = Fraction(PG,100)
##    gMin = gFrac.denominator
##    pgMin = gFrac.numerator
##    #gSteps = N//gMin
##    #if gSteps <= 0:
##    #    print gFrac, pgMin, gMin, gSteps
##    #    return False
##    #gMax = gSteps*gMin
##    #pgMax = gSteps*pgMin
##    #kd and kg are the multiplicative constants
##    #kdMax = min(dSteps,gMax//dMin,pgMax//pdMin)
##    kgMin = max(1,int(ceil(gMin/dMin)),int(ceil(pgMin/pdMin)))
##    #print N, PD, PG
##    #print dFrac, gFrac
##    #print dSteps,pdMax, dMax
##    #print gSteps, pgMax, gMax
##    #print kdMax, kgMin
##    #if kdMax < 1 or kgMin > gSteps:
##    if kgMin > gSteps:
##        return False
##    #print "It's true"
##    return True
