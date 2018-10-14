# Codejam 2013
# Problem C. Fair and square

import math

#inputFilename = 'problem.input'
inputFilename = 'C-small-attempt0.in'

###################
input = open(inputFilename, 'r').readlines()
casesCount = int(input[0].strip())
cases = {}

# Translate cases into a separate sets: cases
i = 1
while i <= casesCount:
    t = input[i].split(' ')
    cases[i] =  [t[0], t[1].strip()]
    i += 1
    
class Case:
    def __init__(self, case):
        self.min = int(case[0])
        self.max = int(case[1]) + 1
        
    # Is it a palindrome number ?
    def isPalindrome(self, n):
        if n < 10:
            return True
        
        if str(n) == str(n)[::-1]:
            return True
        else:
            return False
    
    # Is it a square of a number ?
    # returns the square root if yes
    # 0 if not
    def getSquareRoot(self, n):
        sqrt = math.sqrt(n)
        if int(sqrt) == sqrt:
            return int(sqrt)
        else:
            return 0
    
    def evaluate(self):
        fairAndSquareCount = 0
        
        for n in range(self.min, self.max):
            if self.isPalindrome(n):
                sqrt = self.getSquareRoot(n)
                if sqrt != 0 and self.isPalindrome(sqrt):
                    fairAndSquareCount += 1
        
        return fairAndSquareCount
        
# Iterate through cases and evaluate to prepare output
for i in cases:
    case = Case(cases[i])
    print 'Case #%s: %s' % (i, case.evaluate())