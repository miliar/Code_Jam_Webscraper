from sys import stdin
import math


class FairSquareFinder:
    """docstring for FairSquareFinder"""
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.numbersOfFairSquare = 0
        self.squaresFairs = []

    def isPalindrome(self, n):
        if isinstance(n, int) or n.is_integer():
            stringX = str(int(n))
            palindrome = True
            j = len(stringX) - 1
            offsetTop = int(math.floor(len(stringX)))
            for x in xrange(0, offsetTop):
                if stringX[x] != stringX[j - x]:
                    palindrome = False
        else:
            palindrome = False

        return palindrome

    def calculateNumberOfFairSquare(self):
        for x in xrange(self.a, self.b + 1):
            if self.isPalindrome(x) and self.isPalindrome(math.sqrt(x)):
                self.squaresFairs.append(x)

        self.numberOfFairSquare = len(self.squaresFairs)

    def getNumberOfFairSquare(self):
        self.calculateNumberOfFairSquare()
        return self.numberOfFairSquare


def main():
    t = 0
    numberCases = 0

    for line in stdin.readlines():
        if t != 0:
            a, b = [int(x) for x in line.rstrip().split(' ')]
            fairSquareFinder = FairSquareFinder(a, b)
            print 'Case #%i: %i' \
                % (t, fairSquareFinder.getNumberOfFairSquare())
        else:
            numberCases = int(line.rstrip())

        t += 1

    if t - 1 != numberCases:
        print 'ERROR! %d != %d' % (t, numberCases)

if __name__ == '__main__':
    main()
