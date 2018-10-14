__author__ = 'Drazen'

import math
from fractions import Fraction


def solve(frac):
    result = math.log(frac.denominator,2)
    temp = 1.0
    counter = 0
    if math.floor(result) != result:
        return 'impossible'
    while temp > frac:
        counter += 1
        temp /= 2.0
    return str(counter)

if __name__ == "__main__":
    inputFile = open('A-small-attempt2.in', mode='r')
    outputFile = open('output.txt', mode='w')
    resultLine = 'Case #{0}: {1}'
    inputFile.seek(0)
    numberOfTests = int(inputFile.readline())
    for i in xrange(numberOfTests):
        P, Q = [int(x) for x in inputFile.readline().split('/')]
        f = Fraction(P,Q)
        outputFile.write(resultLine.format(i+1, solve(f)) + '\n')
    inputFile.close()
    outputFile.close()
