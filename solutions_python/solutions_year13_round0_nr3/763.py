import math

def readFile(filename):
    f = open(filename, 'r')
    totalCases = int(f.readline()[:-1])
    cases = []
    for i in range(totalCases):
        line = f.readline()
        if '\n' in line:
            line = line[:-1]
        case = map(int, line.split(' '))
        cases.append(case)
    f.close()
    return cases


def generatePalindromes(minV, maxV):
    minLen = int( len(str(minV)) / 2 )
    maxLen = int( len(str(maxV)) / 2 )
    palindromes = []
    if minLen == 0:
        for num in range(10):
            if minV <= num <= maxV:
                palindromes.append(num)
                #yield num
    if maxLen == 0:
        #yield
        return palindromes
    m = pow(10, minLen-1 if minLen > 0 else minLen)
    M = pow(10, maxLen-1 if maxLen > 0 else maxLen)
    number = m
    while len(str(number) + str(number)) <= len(str(maxV)):
        palindrome = int(str(number) + str(number)[::-1])
        if minV <= palindrome <= maxV:
            palindromes.append(palindrome)
            #yield palindrome
        if len(str(palindrome)) == len(str(maxV)):
            number += 1
            continue
        for d in range(10):
            palindrome = int(str(number) + str(d) + str(number)[::-1])
            if minV <= palindrome <= maxV:
                #yield palindrome
                palindromes.append(palindrome)
        number += 1
    #print len(palindromes)
    return palindromes

def isPalindrome(number):
    return str(number) == str(number)[::-1]

def getRoots(minV, maxV):
    minRoot = int(math.sqrt(minV))
    maxRoot = int(math.sqrt(maxV))
    return minRoot, maxRoot

def findfns(infile, outfile):
    cases = readFile(infile)
    output = []
    for index, (minV, maxV) in enumerate(cases):
        minRoot, maxRoot = getRoots(int(minV), int(maxV))
        square = int(math.pow(minRoot, 2))
        if minRoot ** 2 < int(minV):
            minRoot += 1
        counter = 0
        palindromes = generatePalindromes(minRoot, maxRoot)
        #print palindromes
        for number in palindromes:
            square = int(math.pow(number, 2))
            if square < int(minV) or square > int(maxV):
                continue
            if isPalindrome(square):
                counter += 1
                #print str(square) + " is a fair and square number because " + str(number) + ' is a palindrome. Diff to destination = ' + str(maxV - square)
        output.append('Case #' + str(index + 1) + ": " + str(counter))
        #print 'Between ' +  str(minV) + ' and ' + str(maxV) + ' there are ' + str(counter) + ' fns numbers.'
    output = '\n'.join(output)
    f = open(outfile, 'w')
    f.write(output)
    f.close()


infile = 'C-large-1.in'
outfile = 'C-large.out'
findfns(infile, outfile)
#findPalindromes(10, 120)