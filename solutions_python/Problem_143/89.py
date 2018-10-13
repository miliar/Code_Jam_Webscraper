__author__ = 'Gantmajer'

''' I'm using the numpy library. http://www.numpy.org/ '''
from numpy import array

if __name__ == '__main__':
    inFile = open('B-large.in', 'r')
    numberOfTests = int(inFile.readline())
    outFile = open('B-large.out', 'w')
    for i in range(1, numberOfTests + 1):
        numbers = [int(elem) for elem in inFile.readline().split()]
        high = max(numbers[0:2])
        low = min(numbers[0:2])
        k = numbers[2]
        if k > high or k > low:
            result = high * low
        else:
            result = high * k + k * (low - k)
            for elem1 in range(k, high):
                for elem2 in range(k, low):
                    if (elem1 & elem2) < k:
                        result += 1
        outFile.write('Case #%d: %d\n' % (i, result))