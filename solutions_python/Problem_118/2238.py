sample    = 'sample.txt'
smallData = 'C-small-attempt0.in'
largeData = ''
output    = 'output.txt'

def isPalindrome(x):
    if int(x) != x:
        return False
    
    strX = str(int(x))
    reversedStrX = strX[::-1]
    return True if strX == reversedStrX else False

# Test isPalindrome(x)
def testIsPalindrome():
    testCaseList = [6, 11, 121, 10, 12, 223, 2244, 3.0, 14.0]
    resultList   = [True, True, True, False, False, False, False, True, False]
    for n, case in enumerate(testCaseList):
        print isPalindrome(case) == resultList[n]

##testIsPalindrome()
        

with open(smallData, 'r') as f, open(output, 'w') as outFile:
    t = int(f.readline())
    print 'T =', t

    for caseNum in xrange(t):
        a, b = map(int, f.readline().split())
        print 'A, B =', a, b

        count = 0
        for n in xrange(a, b + 1):
##            print 'n, n**.5 =', n, n**.5

            if isPalindrome(n):
                if isPalindrome(n**.5):
                    count += 1
                    print 'n, n**.5 =', n, n**.5

        output = 'Case #{0}: {1}\n'.format(caseNum + 1, count)
        print output
        outFile.write(output)
