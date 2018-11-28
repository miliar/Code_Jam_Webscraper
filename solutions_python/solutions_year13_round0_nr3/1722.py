#!/usr/bin/python

import fileinput, math

def is_palindrome(num):
    numstr = str(num)
    for i in range(0, int(len(numstr) / 2)):
        if not numstr[i] == numstr[len(numstr) - 1 - i]:
            return False
    return True

class Case(object):
    casenum = 0
    lower = 0
    upper = 0
    
    solution = -1
    
    def __init__(self, casenum, lower, upper):
        self.casenum = casenum
        self.lower = lower
        self.upper = upper
        
    def solve(self):
        start = int(math.sqrt(self.lower))
        end = math.ceil(math.sqrt(self.upper))
        self.solution = 0
        for i in range(start, int(end + 1)):
            isq = i ** 2
            if isq >= self.lower and isq <= self.upper and is_palindrome(i) and is_palindrome(isq):

                self.solution += 1
        return self.solution
        
    def __str__(self):
        if self.solution == -1:
            self.solve()
            
        return "Case #%i: %i" % (self.casenum, self.solution)
    
if __name__ == "__main__":
    firstline = True
    cases = []
    for line in fileinput.input():
        if firstline:
            firstline = False
            continue
            
        bounds = line.split()
        cases.append(Case(len(cases) + 1, int(bounds[0]), int(bounds[1])))
    
    for case in cases:
        print case
