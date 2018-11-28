import sys
import math

inName = sys.argv[1]
outName = inName[:inName.index('.')] + '.out'

fin = open(inName)
fout = open(outName, 'w')

cases = int(fin.readline())

def pp(case, out):
    ss= "Case #%d: %s\n" % (case+1, out)
    print ss,
    fout.write(ss)



for case in xrange(cases):
    [X, R, C] = map(int, fin.readline().strip().split(' '))

    res = 'GABRIEL'

    # Odd number of spaces, can't possibly be filled
    if R * C % X != 0:
        res = 'RICHARD'

    # Square dimentions of N x N omino exceed box size
    longestSquareSide = math.ceil(math.sqrt(X))
    if (longestSquareSide > R or longestSquareSide > C) and X > 2:
        res = 'RICHARD'

    # Long dimentions of omino exceed both box sides
    if X > R and X > C:
        res = 'RICHARD'

    # t-shape
    #   #
    #  ##
    #   #
    #
    if R == 4 and C == 2 or R == 2 and C == 4:
        if X == 4:
            res = 'RICHARD'

    if R == 3 and C == 4 or R == 4 and C == 3:
        if X == 6:
            res = 'RICHARD'

    # with 7+, an enclosed area is possible
    if X >= 7:
        res = 'RICHARD'

    pp(case, res)

fout.close()
