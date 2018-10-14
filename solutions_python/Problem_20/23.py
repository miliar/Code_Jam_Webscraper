inputFileName = "D-small-attempt2.in"
outputFileName = "D-small-attempt2.out"
DEBUG = True
PSYCO = False

import sys
import math

if PSYCO :
    try :
        import psyco
        psyco.full()
    except :
        pass

def dprint(s) :
    if DEBUG :
        sys.stderr.write(str(s))

################################################################################
# algorithm
################################################################################

cache = {}

def solve(H, W, rocks, x0, y0) :
    if (x0, y0) in cache :
        return cache[(x0, y0)]
    if x0 == W and y0 == H :
        return 1
    if x0 > W or y0 > H or (x0 , y0 ) in rocks :
        return 0
    else :
        ans = solve(H, W, rocks, x0 + 1, y0 + 2) + solve(H, W, rocks, x0 + 2, y0 + 1)
        cache[(x0, y0)] = ans
        return ans

def solveCase(fileIn):
    H, W, R = [int(x) for x in fileIn.readline().split()]
    rocks = []
    for i in range(R):
        r, c = [int(x) for x in fileIn.readline().split()]
        rocks += [(c, r)]
    global cache
    cache = {}
    return solve(H, W, rocks, 1, 1) % 10007

################################################################################
# main
################################################################################

def main():
    import sys
    fileIn = open(inputFileName)
    if outputFileName == "stdout":
        fileOut = sys.stdout
    else:
        fileOut = open(outputFileName, "w")
    N = int(fileIn.readline())
    dprint("%d cases\n" % N)
    for i in range(N):
        dprint("Entering case %d\n" % (i+1))
        ans = solveCase(fileIn)
        dprint("Case #%d: %s\n" % ((i+1), ans))
        fileOut.write("Case #%d: %s\n" % ((i+1), ans))
    fileIn.close()
    if outputFileName != "stdout":
        fileOut.close()

if __name__== "__main__":
    main()
