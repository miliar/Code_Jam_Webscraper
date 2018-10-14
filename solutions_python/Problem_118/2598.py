'''
Created on Mar 31, 2013

@author: kinsp1
https://code.google.com/codejam/contest/90101/dashboard#s=p0
'''

import math

'''
Created on Mar 31, 2013

@author: kinsp1
'''

answerDict = dict()


def palindromeRecursive(base, maxChars, step):
    if step=='':
        value = base
    else:
        value = step + base + step
    
    if value != '':
        intValue = int(value)
        answerDict[intValue * intValue] = intValue
        
    if not len(value) + 2 > maxChars:
        for i in range(10):
            palindromeRecursive(value, maxChars, str(i))
        
        
#maxChars always more than 1, is inclusive
def buildAnswerSet(maxChars):
    palindromeRecursive('', maxChars, '')
    for i in range(10):
        palindromeRecursive(str(i), maxChars, '')
        

def isPalindrome(number):
    strNum = str(number)
    for i in range(math.floor(len(strNum)/2)):
        #print(":{0}".format(strNum[-(1+i)]))
        if not strNum[i] == strNum[-(1+i)]:
            return False
    
    return True        
        

def processInterval(start, end):
    hits = 0
    for i in range(start, end+1):
        if i in answerDict and isPalindrome(i):
            hits = hits + 1
    return hits


    

if __name__ == '__main__':
    inputFile = open('C-small-attempt0.in', 'r')
    outputFile = open('outputFile', 'w')
    outputFile.truncate()
    #4 for 1000, why not
    #8 for 10**14
    buildAnswerSet(4)
    
    print("done building")

    
    testCount = int(inputFile.readline())

    for i in range(testCount):
        #print("Test{}:".format(i))
        start, end = inputFile.readline().split()
        start, end = int(start), int(end)
        print("Case #{0}: {1}".format(1+i, processInterval(start, end)), file=outputFile)
        
    
        
    
    
    