import itertools
import math
import operator

class FAS:
        
    def fair_and_square(self):
        inputFile = open('input.txt','r')
        outputFile = open('output.txt','w')
        numTestCases = int(inputFile.readline())
        for tc in range(0,numTestCases):

            numFairSquare = 0

            lower, upper = [int(x) for x in inputFile.readline().split(' ')]

            lowerRoot = int(math.ceil(math.pow(lower, 0.5)))
            upperRoot = int(math.floor(math.pow(upper, 0.5)))

            for i in range(lowerRoot, upperRoot+1):
                if self.isPalindrome(i):
                    square = i*i
                    if (self.isPalindrome(square)):
                        numFairSquare += 1

            outputString = 'Case #%d: %d\n'%(tc+1,numFairSquare)
            outputFile.write(outputString)
            print outputString
            
    def isPalindrome(self, num):
        numString = '%d'%num
        reverseString = ''

        for j in range(len(numString),0,-1):
            reverseString += numString[j-1]

        if numString == reverseString:
            return True

        return False

if __name__ == '__main__':
    fas = FAS()
    fas.fair_and_square()