import sys
import time

palindromeCache = dict()
palindromeSquareCache = dict()
def isPalindrome(a):
    if a in palindromeCache.keys():
        return True
    strA = str(a)
    
    b = list(strA)
    b.reverse()
    
    c = int(''.join(b))
    
    if c == a:
        palindromeCache[a]=a
        
        return True
    return False

def isPalindromeSquare(a):
    if a in palindromeSquareCache.keys():
        return True
    if isPalindrome(a):
        
        root = a**.5
        
        if int(root) != root:
            return False
        if isPalindrome(int(root)):
            palindromeSquareCache[a] = a
            return True
        
    return False

def perform(fileLocation):
    inputFile = open(fileLocation,'r')
    outputFile = open(fileLocation.replace('.in','.out'),'w')
    testCase = int(inputFile.readline())
    lineNumber = 1
    while 1:
        firstLine = inputFile.readline()
        if firstLine == '':
            inputFile.close()
            outputFile.close()
            return
        Numbers=map(int,firstLine.split(' '))
        start = Numbers[0]
        stop = Numbers[1]
        
        requiredNo = 0
        for i in xrange(start,stop+1):
            if isPalindromeSquare(i):
               
                requiredNo += 1
        
        outputFile.write('Case #%d: %d\n'%(lineNumber,requiredNo))
        
        lineNumber += 1
if __name__ == '__main__':
    startTime = time.time()
    perform(sys.argv[1])
    stopTime = time.time()
    print 'time :',stopTime - startTime



        



