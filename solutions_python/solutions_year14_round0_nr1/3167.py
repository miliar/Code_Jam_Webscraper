import sys
import numpy as np


def readGrid(filehandle):
    grid = np.zeros((4, 4))
    for index in xrange(0, 4):
        line = filehandle.readline()
        grid[index,] = np.array([ int(v) for v in line.split(" ") ])
    return grid

def readRowAsInt(filehandle):
    return int(filehandle.readline())

def main():
    filehandle = open(sys.argv[1], 'r')
    numTestCases = readRowAsInt(filehandle)

    for index in xrange(0, numTestCases):
        guess1 = readRowAsInt(filehandle)
        grid1 = readGrid(filehandle)
        guess2 = readRowAsInt(filehandle)
        grid2 = readGrid(filehandle)

        possibilities = set(grid1[guess1 - 1]).intersection(set(grid2[guess2 - 1]))

        if len(possibilities) == 1:
            print "Case #{0}: {1}".format(str(index + 1), int(list(possibilities)[0]))
        elif len(possibilities) == 0:
            print "Case #{0}: Volunteer cheated!".format(str(index + 1))
        else:
            print "Case #{0}: Bad magician!".format(str(index + 1))

        
if __name__ == "__main__":
    main()
