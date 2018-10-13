'''
Created on 14/04/2013

@author: George
'''
import math
f = open("C-small-attempt0.in").read().split("\n")
out = open("out.txt", "a")

def testPalindrome(string):
    string = str(string)
    return string == string[::-1]


caseCount = int(f[0])
solutions = {}
for each in range(1, caseCount+1):
    solutions[each] = 0
    (start, stop) = f[each].split(" ")
    (startRoot, stopRoot) = (int(math.ceil(math.sqrt(int(start)))), int(math.floor(math.sqrt(int(stop)))) )

    for number in range(startRoot, stopRoot+1):
        if testPalindrome(number):
            if testPalindrome(number**2):
                solutions[each] = solutions[each] + 1
                
                #print "#%s:" %each, number, number**2, "is a match?"

        
    print >>out, "Case #%s: %s" %(each, solutions[each])





