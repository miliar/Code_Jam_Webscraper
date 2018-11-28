import time
import math

debug = False

tStart = time.time()

fname = "C-small-attempt1"
#fname = "fairtest"

fin = open(fname+".in","r")

flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

for icase in range(1,numcases+1):

    line = flines[icase].split()
    A = int(line[0])
    B = int(line[1])

    fairandsquare = 0

    squaremin = int(math.ceil(A**.5))
    squaremax = int(math.floor(B**.5))

    for sq in xrange(squaremin,squaremax+1):
        # is root a palindrome?
        strval = str(sq)
        if strval == strval[::-1]:
            # is square a palindrome?
            testval = sq*sq
            strval = str(testval)
            if strval == strval[::-1]:
                fairandsquare += 1     
    
    outstr = "Case #%d: %d" % (icase,fairandsquare)
    print outstr
    fout.write("%s\n" % (outstr))
    
fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))

    

            
