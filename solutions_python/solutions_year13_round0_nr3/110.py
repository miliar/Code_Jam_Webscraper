
import itertools
import math

def squares():
    """Generates all square numbers starting from 1"""
    for n in itertools.count(1):
        yield n ** 2

def fairNSquare():
    """Generates all fair and square numbers!"""
    yield 1
    yield 4
    yield 9
    previousNDigitRoots = ['1','2','3']
    for ndigits in itertools.count(2):
        currentNDigitRoots = []
        #if odd
        if ndigits % 2:
            #old numbers have even ndigits
            for oldRoot in previousNDigitRoots:
                #add 0...2 in the middle
                for i in range(3):
                    newRoot = oldRoot[:ndigits/2] + str(i) + oldRoot[ndigits/2:]
                    p = int(newRoot) ** 2
                    if ispalindrome(p):
                        yield p
                        currentNDigitRoots.append(newRoot)
        else:
            for oldRoot in previousNDigitRoots:
                #old numbers have odd ndigits, so duplicate middle digit
                newRoot = oldRoot[:ndigits/2] + oldRoot[ndigits/2-1:]
                p = int(newRoot) ** 2
                if ispalindrome(p):
                    yield p
                    currentNDigitRoots.append(newRoot)
        previousNDigitRoots = currentNDigitRoots

def fairNSquareRoots():
    """Generates palindromes which are potentially the sqrt of other
    palindromes"""
    yield 1
    yield 2
    yield 3
    innerdigits = "012"
    for ndigits in itertools.count(2):
        isodd = bool(ndigits % 2)
        #roots starting with 1
        ngroups = (ndigits + 1) // 2
        groups = ['1'] + [innerdigits] * (ngroups - 1)
        for result in itertools.product(*groups):
            if isodd:
                digits = ''.join(result) + ''.join(reversed(result[:-1]))
            else:
                digits = ''.join(result) + ''.join(reversed(result))
            yield int(digits)
        #roots starting with 2
        digits = '2' + '0' * (ndigits - 2) + '2'
        yield int(digits)
        if isodd:
            nzerosPerSide = (ndigits - 3) / 2
            zerosOnSide = '0' * ((ndigits - 3) / 2)
            digits = '2' + zerosOnSide + '1' + zerosOnSide + '2'
            yield int(digits)

def palindromes():
    """Generates all palindromes in increasing order starting from 1"""
    outerdigits = "123456789"
    innerdigits = "0123456789"
    for ndigits in itertools.count(1):
        isodd = bool(ndigits % 2)
        ngroups = (ndigits + 1) // 2
        groups = [outerdigits] + [innerdigits] * (ngroups - 1)
        for result in itertools.product(*groups):
            if isodd:
                digits = ''.join(result) + ''.join(reversed(result[:-1]))
            else:
                digits = ''.join(result) + ''.join(reversed(result))
            yield int(digits)

def ispalindrome(n):
    s = str(n)
    return s == ''.join(reversed(s))

fairNSquareCache = []

def solve(f):
    if not fairNSquareCache:
        maxn = 10**100
        for p in fairNSquare():
            if p <= maxn:
                fairNSquareCache.append(p)
            else:
                print "done making cache"
                break
    line1 = next(f)
    lo, hi = map(int, line1.split())

    #a ninja wrote this version
    result = 0
    for p in fairNSquareCache:
        if p > hi:
            return result
        if p >= lo:
            result += 1
    return result

    #fast version
    result = 0
    for root in fairNSquareRoots():
        p = root ** 2
        if not ispalindrome(p):
            continue
        if p > hi:
            return result
        if p >= lo:
            result += 1
            #print p, "sq of", root

    #original slow version
    knownpalindromes = set()
    result = 0
    for p in palindromes():
        if p > hi:
            return result
        knownpalindromes.add(p)
        if p >= lo and math.sqrt(p) in knownpalindromes:
            result += 1
            print p, "sq of", int(math.sqrt(p))

def main(infile, outfile):
    with open(infile, 'r') as f:
        with open(outfile, 'w') as f2:
            cases = int(next(f))
            for i in range(cases):
                print "solving case #{}".format(i+1)
                solution = solve(f)
                f2.write("Case #{}: {}\n".format(i+1, solution))

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:3])

