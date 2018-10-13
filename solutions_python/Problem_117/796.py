
import sys
import pandas as pd


def mul(x, y):
    return x * y

def sumprod(x, y):
    return sum(map(mul, x, y))


if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg;

    #check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):
        x = inputfile.readline().rstrip('\r\n')
        x = map(int, x.split(' '))
        #print x
        N = x[0]
        M = x[1]

        matrix = list()

        for i in range(N):
            x = inputfile.readline().rstrip('\r\n')
            matrix.append(map(int, x.split(' ')))

        matrixDF = pd.DataFrame(matrix)
        #print matrixDF

        result = "YES"
        #print "N" + str(range(N))
        #print "M" + str(range(M))
        for i in range(N):
            for j in range(M):
                #print i, j
                value = matrixDF[j][i]
                #print "value: " + str(value)
                #print matrixDF.ix[i]
                #print matrixDF.ix[::,j]
                if not (False in [a <= value for a in matrixDF.ix[i]]):
                    continue
                elif not (False in [a <= value for a in matrixDF.ix[::,j]]):
                    continue
                else:
                    result = "NO"
                    #print "NO"
                    break



        #print matrix

        outputline = "Case #" + str(m + 1) + ": " + result + "\n"
        print outputline
        outputfile.write(outputline)

