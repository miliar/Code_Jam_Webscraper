def isPalindrome(n):
    s = "{:d}".format(n)
    for i in range(0, (len(s)+1)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def generateList(maxNumber):
    from math import sqrt
    res = [ n**2 for n in range(1, int(sqrt(maxNumber))+1)
            if isPalindrome(n) and isPalindrome(n ** 2) ]
    res.sort()
    return res

def generateListTwoOnes(logMaxSqrt):
    return [ 10**n+1 for n in range(1, logMaxSqrt+1) ]

def generateListThreeOnes(logMaxSqrt):
    return [ 10**n + 10**(n//2) + 1 
             for n in range(2, logMaxSqrt+1, 2) ]

def generateListFourOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 10**n2 + 1 
             for n1 in range(1, logMaxSqrt+1)
             for n2 in range(1, (n1-1) // 2 + 1) ]

def generateListFiveOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 10**(n1//2) + 10**n2 + 1 
             for n1 in range(2, logMaxSqrt+1, 2) 
             for n2 in range(1, (n1-1) // 2 + 1) ]

def generateListSixOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 10**(n1-n3) + 10**n3 + 10**n2 + 1 
             for n1 in range(1, logMaxSqrt+1)
             for n2 in range(1, (n1-1) // 2 + 1) 
             for n3 in range(n2+1, (n1-1) // 2 + 1) ]

def generateListSevenOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 10**(n1-n3) + 10**(n1//2) 
             + 10**n3 + 10**n2 + 1 
             for n1 in range(2, logMaxSqrt+1, 2) 
             for n2 in range(1, (n1-1) // 2 + 1) 
             for n3 in range(n2+1, (n1-1) // 2 + 1) ]

def generateListEightOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 10**(n1-n3) + 10**(n1-n4)
             + 10**n4 + 10**n3 + 10**n2 + 1 
             for n1 in range(1, logMaxSqrt+1)
             for n2 in range(1, (n1-1) // 2 + 1) 
             for n3 in range(n2+1, (n1-1) // 2 + 1) 
             for n4 in range(n3+1, (n1-1) // 2 + 1) ]

def generateListNineOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 10**(n1-n3) + 10**(n1-n4) 
             + 10**(n1//2) + 10 ** n4 + 10**n3 + 10**n2 + 1 
             for n1 in range(2, logMaxSqrt+1, 2) 
             for n2 in range(1, (n1-1) // 2 + 1) 
             for n3 in range(n2+1, (n1-1) // 2 + 1) 
             for n4 in range(n3+1, (n1-1) // 2 + 1) ]

def generateListOneTwoAndTwoOnes(logMaxSqrt):
    return [ 10**n + 2*10**(n//2) + 1 
             for n in range(2, logMaxSqrt+1, 2) ]

def generateListOneTwoAndFourOnes(logMaxSqrt):
    return [ 10**n1 + 10**(n1-n2) + 2*10**(n1//2) + 10**n2 + 1 
             for n1 in range(2, logMaxSqrt+1, 2) 
             for n2 in range(1, (n1-1) // 2 + 1) ]

def generateListTwoTwos(logMaxSqrt):
    return [ 2*10**n+2 for n in range(1, logMaxSqrt+1) ]

def generateListTwoTwosAndOneOne(logMaxSqrt):
    return [ 2*10**n + 10**(n//2) + 2
             for n in range(2, logMaxSqrt+1, 2) ]

def generateListNew(logMaxNumber):
    res = [ 1,2,3 ]
    logMaxSqrt = logMaxNumber // 2
    res.extend(generateListTwoOnes(logMaxSqrt))
    res.extend(generateListThreeOnes(logMaxSqrt))
    res.extend(generateListFourOnes(logMaxSqrt))
    res.extend(generateListFiveOnes(logMaxSqrt))
    res.extend(generateListSixOnes(logMaxSqrt))
    res.extend(generateListSevenOnes(logMaxSqrt))
    res.extend(generateListEightOnes(logMaxSqrt))
    res.extend(generateListNineOnes(logMaxSqrt))
    res.extend(generateListOneTwoAndTwoOnes(logMaxSqrt))
    res.extend(generateListOneTwoAndFourOnes(logMaxSqrt))
    res.extend(generateListTwoTwos(logMaxSqrt))
    res.extend(generateListTwoTwosAndOneOne(logMaxSqrt))
    for n in res:
        if not isPalindrome(n) or not isPalindrome(n**2):
            print("Error with {:d}".format(n))
    res.sort()
    return [ n**2 for n in res ]

if __name__ == "__main__":
    from sys import argv
    from math import sqrt
    from bisect import bisect_left, bisect_right
    fasNumbers = generateListNew(100)
    inputFile = open(argv[1] + ".in", "r")
    outputFile = open(argv[1] + ".out", "w")
    numCases = int(inputFile.readline())
    for caseIdx in range(numCases):
        line = inputFile.readline()
        words = line.split()
        a = int(words[0])
        b = int(words[1])
        res = bisect_right(fasNumbers, b) - bisect_left(fasNumbers, a)
        outputFile.write("Case #{:d}: {:d}\n"
                         .format(caseIdx+1, res))
        
