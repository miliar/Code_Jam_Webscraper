# Run with Python 3.2

import math, sys, time, itertools

input_filename = "Clarge2.txt"

# http://stackoverflow.com/questions/15390807/integer-square-root-in-python
# math.sqrt(n) is wrong for large n as it returns a float
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def nextSquare(x):
    """Returns lowest square number >= x"""
    y = isqrt(x)
    while y*y < x:
        y += 1
    return y*y

def prevSquare(x):
    """Returns highest square number <= x"""
    y = isqrt(x)
    return y*y

def checkInt(x):
    #assert x == int(x), "Not an integer"
    return int(x)

def prevPalindrome(x):
    """Returns highest palindrome <= x"""
    digits = len(str(checkInt(x)))

def isPalindrome(x):
    """Returns True if the number is a palindrome"""
    #return True
    x = str(checkInt(x))
    return x == x[::-1]

def countDigits(x):
    return len(str(checkInt(x)))

def reverseNumber(x):
    return int(str(x)[::-1])

def isPalindromicPrefix(k, L):
    """Returns true if palindromic numbers with palindromic squares could
    possibly start with k (which has digit length L)"""
    sig = L-2 # number of digits to compare
    if sig <= 0: return True
    left = str(k**2)[:sig]
    while sig > 0 and left[len(left)-1] == '9':
        sig -= 1
        left = left[:-1]
    right = str(reverseNumber(k)**2)[-sig:]
    if len(right) < len(left):
        right = "0" * (len(left) - len(right)) + right
    #print(k)
    #print(sig)
    #print(left)
    #print(right)
    #print(left==right[::-1])
    return left == right[::-1]

def getPalindromicPrefixesOfDigitLength(L):
    """Brute-forces palindromic prefixes"""
    rv = []
    for k in range(10**(L-1), 10**L):
        if isPalindromicPrefix(k, L):
            rv += [k]
    return rv

def getPalindromicPrefixesOfDigitLength2(L, prefixesOfPrefixes, popLength):
    """Same as getPalindromicPrefixesOfDigitLength but uses an array
    of shorter prefixes to speed up searching.
    popLength is the length in digits of each element in prefixesOfPrefixes."""
    rv = []
    iteratedDigits = L - popLength
    popShift = 10**iteratedDigits
    for pop in prefixesOfPrefixes:
        shiftedPop = pop * popShift
        for k in range(0, popShift):
            test = shiftedPop + k
            if isPalindromicPrefix(test, L):
                rv += [test]
    return rv

def getPalindromicPrefixesOfDigitLength3(L, step=2):
    """Uses getPalindromicPrefixesOfDigitLength and
    getPalindromicPrefixesOfDigitLength2 to get all prefixes of a certain
    length efficiently"""
    length = 4
    rv = getPalindromicPrefixesOfDigitLength(length)
    while length < L:
        newLength = min(L, length + step)
        rv = getPalindromicPrefixesOfDigitLength2(newLength, rv, length)
        length = newLength
        print(length,len(rv))
    return rv
    

if True:
    maxPrefixLength = 7
    stime = time.time()
    prefixes = {}
    prefixes[1] = getPalindromicPrefixesOfDigitLength(1)
    for k in range(2, maxPrefixLength + 1):
        prefixes[k] = getPalindromicPrefixesOfDigitLength2(k, prefixes[k-1], k-1)
        print(k, len(prefixes[k]))
    #prefixes = getPalindromicPrefixesOfDigitLength3(pdPrefixLength, 1)
    etime = time.time()
    #print('generated prefixes, length '+str(pdPrefixLength)+', in '+str(etime-stime)+' seconds')
    #print('%i prefixes' % len(prefixes))
    #print(prefixes)

if False:
    p1 = getPalindromicPrefixesOfDigitLength3(8, 3)
    p2 = getPalindromicPrefixesOfDigitLength3(8, 1)
    for k in p1:
        if k not in p2:
            print(k)

def permutations(alphabet, length, minPrefix, maxPrefix, skipFirst=False):
    if length == 0:
        yield ""
        return
    for a in permutations(alphabet, length-1, minPrefix[:-1], maxPrefix[:-1]):
        if a < minPrefix[:-1] or a > maxPrefix[:-1]:
            continue
        for b in alphabet:
            if skipFirst and b == alphabet[0]:
                continue
            yield a + b

def radixRange(a, b, r):
    """ Like range(a, b+1) but returned numbers have no digits >= r """
    if countDigits(a) < countDigits(b):
        mid = 10**(countDigits(b) - 1) - 1
        for x in concatIterators(radixRange(a, mid, r), radixRange(mid+1, b, r)):
            yield x
        return
    for x in permutations("0123456789"[:r], countDigits(a), str(a), str(b)):
        i = int(x)
        if i >= a and i <= b:
            yield i
        
def concatIterators(a, b):
    for x in a: yield x
    for x in b: yield x

def product(L):
    x = 1
    for k in L:
        x *= k
    return x

def factorial(n):
    return product(range(1, n+1))

def selections(n, r):
    """returns unique unordered selections of r elements from {0..n-1}"""
    return list(itertools.combinations(range(n), r))

def wholeNumberFromFirstDigits(firstDigits, iteratedDigitShift, digits):
    wholeNumber = firstDigits * iteratedDigitShift
    if (digits % 2) == 1:
        if digits > 1:
            wholeNumber += reverseNumber(firstDigits//10)
    else:
        wholeNumber += reverseNumber(firstDigits)
    return wholeNumber

def precalc(start, end, usePrefixes=True):
    """Returns a list of palindromic numbers with palindromic squares
    where the squares are between start and end (inclusive)."""
    start = isqrt(nextSquare(start))
    end = isqrt(prevSquare(end))
    n = []
    
    minDigits = countDigits(start)
    maxDigits = countDigits(end)
    for digits in range(minDigits, maxDigits+1):

        print(digits, len(n))
        
        # Only iterate over the first ceil(digits/2) digits.
        # If the number is a palindrome, the rest can be determined from those.

        numIteratedDigits = math.ceil(digits/2)
        numFixedDigits = digits - numIteratedDigits
        iteratedDigitShift = 10 ** numFixedDigits

        firstDigitsMin = 10**(numIteratedDigits-1)
        firstDigitsMax = 10**numIteratedDigits

        maxThisDigit = 10**numIteratedDigits

        minMaxes = [[firstDigitsMin, firstDigitsMax]]

        usedPrefixLength = min(maxPrefixLength, digits//2)

        if usePrefixes and usedPrefixLength in prefixes:
            # use precalculated prefixes
            # which all returned numbers must start with
            numActuallyIteratedDigits = numIteratedDigits - usedPrefixLength
            minMaxes = [
                [checkInt((10**numActuallyIteratedDigits) * prefix),
                 checkInt((10**numActuallyIteratedDigits) * (prefix + 1))]
                    for prefix in prefixes[usedPrefixLength]]

        # Empirical observation: By this point (sometime before digits=15) all numbers have
        # only 0 and 1 digits, or are of the form 20000000..000000002
        # or 2000000..000010000..00000002
        # or 1000...0001000...0002000...0001000...0001
        # or 1000...0002000...0001
        numbersWithTwo = [2 * (10**(numIteratedDigits - 1))]
        if (digits % 2) == 1:
            numbersWithTwo += [2 * (10**(numIteratedDigits - 1)) + 1]
            numbersWithTwo += [(10**(numIteratedDigits - 1)) + 2]

            for onePos in range(1, numIteratedDigits - 1):
                numbersWithTwo += [(10**(numIteratedDigits - 1)) + (10**onePos) + 2]

        # numbersWithTwo stores these exceptions, and the rest of
        # the numbers we consider contain only 0 and 1.

        # The numbers that do not contain a 2 contain 1 to 5 (inclusive)
        # 1-digits in their first ceil(digits/2) digits, including the
        # leading 1, and all such numbers are valid.

        if digits > 8:
            for test in numbersWithTwo:
                test = wholeNumberFromFirstDigits(test, iteratedDigitShift, digits)
                if test >= start and isPalindrome(test**2) and test <= end:
                    n += [test]
            for numsel in range(0, 5):
                for x in selections(numIteratedDigits - 1, numsel):
                    test = 10 ** (numIteratedDigits - 1)
                    for k in x:
                        test += 10 ** k
                    test = wholeNumberFromFirstDigits(test, iteratedDigitShift, digits)
                    #print(test)
                    if test >= start and isPalindrome(test**2) and test <= end:
                        n += [test]
            continue

        for firstDigitsMin, firstDigitsMax in minMaxes:
            if firstDigitsMin >= maxThisDigit: continue
            
            for firstDigits in range(firstDigitsMin, firstDigitsMax):
                wholeNumber = firstDigits * iteratedDigitShift
                if (digits % 2) == 1:
                    if digits > 1:
                        wholeNumber += reverseNumber(firstDigits//10)
                else:
                    wholeNumber += reverseNumber(firstDigits)

                #assert isPalindrome(wholeNumber)
                if wholeNumber >= start and isPalindrome(wholeNumber**2) and wholeNumber <= end:
                    n += [wholeNumber]
                    #print(wholeNumber,wholeNumber**2)

    return n

def countSolutions(start, end, allSolutions):
    start = checkInt(nextSquare(start)**0.5)
    end = checkInt(prevSquare(end)**0.5)
    
    n = 0
    for k in allSolutions:
        if k >= start and k <= end:
            n += 1
    return n

class BinTree(object):
    def __init__(self, minval, maxval, nums):
        self.min = minval
        self.max = maxval
        self.centre = (minval + maxval) / 2
        self.count = len(nums)
        if len(nums) <= 200:
            self.values = nums
        else:
            self.values = None
            left = [x for x in nums if x < self.centre]
            right = [x for x in nums if x >= self.centre]
            self.left = BinTree(min(left), max(left), left)
            if len(right) == 0:
                self.right = BinTree(0, 0, right)
            else:
                self.right = BinTree(min(right), max(right), right)

    def countInclusiveInterval(self, min, max):
        if max < self.min or min > self.max:
            return 0

        if min < self.min and max > self.max:
            return self.count

        if self.values != None:
            n = 0
            for k in self.values:
                if k >= min and k <= max:
                    #print(k,min,max)
                    n += 1
            return n

        return self.left.countInclusiveInterval(min, max) + self.right.countInclusiveInterval(min, max)


if True:
    pcStart = 1
    pcEnd = 10**100
    solutionsTree = BinTree(pcStart, pcEnd, [x*x for x in precalc(pcStart, pcEnd)])
    
    if False:
        with open("all.txt", "w") as f:
            s = ""
            for n in precalcData:
                s += str(n)+"\n"
            f.write(s)
    
    with open(input_filename, "r") as infile:
        with open("output.txt", "w") as sys.stdout:
            numCases = int(infile.readline())
            for case in range(1,numCases+1):
                start, end = infile.readline().replace("\n","").split(" ")
                start = int(start)
                end = int(end)
                if start < pcStart:
                    raise Exception("Did not precalculate numbers before "+str(pcStart))
                if end > pcEnd:
                    raise Exception("Did not precalculate numbers after "+str(pcStart))
                print("Case #%i: %i" % (case, solutionsTree.countInclusiveInterval(start, end)))








