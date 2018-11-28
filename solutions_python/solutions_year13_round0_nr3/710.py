'''
Created on Apr 13, 2013

@author: Sean Groathouse
'''
memo = {}

# Returns a list of palindromes with exactly n digits
def getPalindromesOfLength(n):
    palindromes = list()
    nIsOdd = (n % 2 == 1)
    lastDigit = (n+1)/2 # Due to symmetry, the remaining digits don't matter
    powTen = 1
    for _i in range(lastDigit-1):
        powTen *= 10
    numPalindromes = (9 * (powTen))
    digits = ""
    digits += "1"
    for _digit in range(1, lastDigit):
        digits += "0"
    for _i in range(numPalindromes):
        reverse = digits[::-1]
        if nIsOdd:
            reverse = reverse[1:] # Don't double the middle if it's odd length
        numbStr = digits + reverse
        number = int(numbStr)
        palindromes.append(number)
        newFirst = int(digits) + 1
        digits = str(newFirst)
    return palindromes

# Returns a list of palindromes with at most n digits
def getPalindromes(n):
    if n in memo:
        return memo[n]
    palindromes = list()
    for i in range(n):
        part = getPalindromesOfLength(i+1)
        palindromes = palindromes + part
    memo[n] = palindromes
    return palindromes

# Squares each integer in the given list
def squareList(inlist):
    outlist = list()
    for i in range(len(inlist)):
        outlist.append(inlist[i] * inlist[i])
    return outlist

def howManyPalindromes(inlist):
    numPal = 0
    for item in inlist:
        if (isPalindrome(item)):
            numPal += 1
    return numPal

def isPalindrome(n):
    string = str(n)
    lastDigit = (len(string) / 2)
    end = len(string) - 1
    for i in range(lastDigit):
        if string[i] != string[end-i]:
            return False
    return True

fin = open('C-large-1.in', 'r')
finput = fin.readlines()
fin.close()
it = iter(finput)
numbCases = (int)(it.next())
output = ""

for case in xrange(numbCases):
    line = (it.next().rstrip().split())
    a = (int)(line[0])
    b = (int)(line[1])
    blen = len(line[1])
    if (blen % 2 == 0):
        rootlen = (blen / 2) + 1
    else:
        rootlen = (blen + 1) / 2
    if rootlen >= 8:
        rootlen = 7 # Large input 1 never exceeds this requirement
    
    palindromes = getPalindromes(rootlen)
    squares = squareList(palindromes)
    validSquares = list()
    for i in range(len(squares)):
        if (squares[i] >= a and squares[i] <= b):
            validSquares.append(squares[i])
    answer = howManyPalindromes(validSquares)
    output += "Case #%d: %d\n" % (case+1, answer)
    
fout = open('large1.txt', 'w')
fout.write(output)
fout.close()