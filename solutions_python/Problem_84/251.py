import sys, re
from fractions import Fraction

def fixsquares(sqdata):
    rows, cols = sqdata[0]

    data = []
    for word in sqdata[1]:
        data.append( list(word) )

    for i in range(rows):
        row = []
        for j in range(cols):
            if data[i][j] == '.': pass
            elif data[i][j] != '#': pass # ignoring prev squared stuff
            else:
                # are we at edge?
                if (i == rows-1) or (j == cols-1): return ["Impossible"]

                # is there a square to be made?
                if (data[i][j+1] == '#') and (data[i+1][j] == '#') and (data[i+1][j+1] == '#'):
                    # yes! make square
                    #print data[i][j]
                    data[i][j] = '/'
                    data[i][j+1] = "\\"
                    data[i+1][j] = "\\"
                    data[i+1][j+1] = '/'
                else:
                    return ["Impossible"]
                
    return data
    


def processtestcases():
    numtestcases = int(sys.stdin.readline().rstrip())
    testcases = []

    for i in range(numtestcases):
        data = []
        dims = [int(a) for a in sys.stdin.readline().rstrip().split(' ')]
        #print dims

        #print "Read data:"
        for j in range(dims[0]):
            picrow = sys.stdin.readline().rstrip()
            data.append( picrow )
            #print picrow

        testcases.append([dims, data])

    return testcases


if __name__ == "__main__":
    testcases = processtestcases()
    #print str(testcases)
    i = 1
    for testcase in testcases:
        print "Case #"+str(i)+":"
        squareimage = fixsquares(testcase)
        for sqline in squareimage:
            print ''.join(sqline)
        i += 1





