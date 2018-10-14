import time
import sys

debug = False

minoperations = sys.maxint

def explore(A,mlist,operations):
    global minoperations
    if debug:
        print A,mlist,operations

    # Absorb all we can absorb
    newind = 0
    for i in xrange(len(mlist)):
        if mlist[i] < A:
            A += mlist[i] # grow as we absorb
            newind = i+1
            if debug:
                print 'absorb %d, new size %d' % (mlist[i],A)
    if newind > 0:
        mlist = mlist[newind:]
    # Now done or need an operation.  Either trim or add.
    done = False
    if len(mlist) == 0:
        done = True
    elif len(mlist) == 1:
        operations += 1
        done = True
    elif A == 1:
        operations = len(mlist) # should do this before the loop
        done = True

    if done:
        if operations < minoperations:
            minoperations = operations
        return

    # Explore two ways
    explore(A+(A-1),mlist,operations+1) # Add a max size
    explore(A,mlist[0:len(mlist)-1],operations + 1)

tStart = time.time()

fname = "A-small-attempt1"
#fname = "motetest"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

for icase in range(1,numcases+1):
   
    line = flines[2*icase-1].split()
    A = int(line[0])
    nummotes = int(line[1])
    line2 = flines[2*icase].split()
    mlist = sorted([int(line2[x]) for x in xrange(nummotes)])

    if debug:
        print A
        print mlist

    minoperations = sys.maxint

    explore(A,mlist,0)
    
    outstr = "Case #%d: %d" % (icase,minoperations)
    print outstr
    fout.write("%s\n" % (outstr))
    
fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))

    

            
