import sys
import re

def read_spaced_line(file):
    line = file.readline()
    #print("Read: '%s'\n"%line,file=sys.stderr)
    return re.split('\s+', line.strip())

import contextlib
@contextlib.contextmanager
def yield_none():
    yield None

@contextlib.contextmanager
def _open_argv_file(argnum, mode='Ur', force_file=False):
    """
    Opens a file specified in arguments.
    If not force_file, stdin/out may be requested by a non existant argument,
    or by specifying '-' as the filename.
    """
    filename = '-'
    if len(sys.argv) >= argnum+1:
        filename = sys.argv[argnum]
        
    if filename == '-':
        if force_file:
            raise ValueError("argv[%d] must indicate a file to open" % argnum)
        
        if mode is None or mode == '' or 'r' in mode:
            fh = sys.stdin
        else:
            fh = sys.stdout
    else:
        fh = open(filename, mode)
    try:
        yield fh
    finally:
        if filename is not '-':
            fh.close()
### END SETUP FUNCTIONS

DEBUG = False


import math
def getSideArea(ri, hi):
    return 2*ri*math.pi * hi
def getTopArea(ri, hi):
    return math.pi * ri*ri


def solve_case(fileIn):
    (N, K) = map(int, read_spaced_line(fileIn)) #or otherwise

    pancakes = []

    for pancakeNum in range(N):
        (ri, hi) = map(int, read_spaced_line(fileIn))
        pancakes.append( (ri, hi, pancakeNum) )

    pancakesBySideArea = [
        (
            getSideArea( pancake[0], pancake[1]),#0
            getTopArea(pancake[0], pancake[1]),#1
            pancake[0],#2 - ri
            pancake[1],#3 - hi
            pancake[2],#4 - indx
        ) for pancake in pancakes
    ]
    pancakesBySideArea.sort()
    pancakesBySideArea.reverse()

    pancakesGuaranteed = pancakesBySideArea[0:K-1] #K-1 are garunteed
    remainingSelection = pancakesBySideArea[K-1:]

    guaranteedExposed = sum(
        [
            pancake[0] for pancake in pancakesGuaranteed
        ]
    ) if K>1 else 0 #Sum of side areas
    
    maxGuaranteedTopArea = max(
        [pancake[1] for pancake in pancakesGuaranteed]
    ) if K>1 else 0
    
    #remaining exposed is radius of max selected pancake
    #plus circum s.a. of new pancake

    #Adding one pancake adds its side area, and its increase in top area

    remainingExposed = [
        (
            pancake[0] + max(pancake[1],maxGuaranteedTopArea)
        ) for pancake in remainingSelection
    ]

    bestSelection = max(remainingExposed)

    bestSyrupArea = bestSelection + guaranteedExposed


    #debug
    if DEBUG:
        print(N,K)
        print(pancakesBySideArea, maxGuaranteedTopArea,
              pancakesGuaranteed, remainingSelection)
        print("Exposed:",guaranteedExposed, remainingExposed)

    return bestSyrupArea
        

    
    

        
        
    #topData = read_spaced_line(fileIn)
    #(N, M, K) = map(int, read_spaced_line(file)) #or otherwise
    #for i in range topData:
    #    innerData = read_spaced_line(fileIn)
    #...etc
    pass




if __name__=='__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: thisfile.py filenamein filenameout", file=sys.stderr)
        sys.exit()
    force_file=not DEBUG and False
        

    with _open_argv_file(1, "rU") as fileIn,\
         _open_argv_file(2, "w", force_file=force_file) as fileOut:

        T = int(fileIn.readline().strip())

        for caseNum0Indexed in range(T):
            caseSoln = solve_case(fileIn)
            print("Case #%d: %s"%(caseNum0Indexed+1,caseSoln), file=fileOut)
        #Done all cases
    #close files

