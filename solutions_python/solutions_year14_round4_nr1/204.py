from scipy.sparse.dia import dia_matrix

__author__ = 'Gantmajer'

''' I'm using the numpy library. http://www.numpy.org/ '''
from numpy import array

if __name__ == '__main__':
    inFile = open('A-large.in', 'r')
    numberOfTests = int(inFile.readline())
    outFile = open('A-large.out', 'w')
    for i in range(1, numberOfTests + 1):
        discSize = int(inFile.readline().split()[1])
        fileSizes = [int(elem) for elem in inFile.readline().split()]
        fileSizes.sort(reverse=True)
        numberOfDiscs = 0
        while fileSizes:
            firstSize = fileSizes.pop(0)
            numberOfDiscs += 1
            if fileSizes and (firstSize + fileSizes[-1]) <= discSize:
                fileSizes.pop()
        outFile.write('Case #%d: %d\n' % (i, numberOfDiscs))