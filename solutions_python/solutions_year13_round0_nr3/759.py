def seq01(n):
    if n==0:
        yield ''
    else:
        for i in '01':
            for sub in seq01(n-1):
                yield i+sub

def makePalinDromeBinary(l):
    if l == 1:
        return [1, 2, 3]
    if l%2 == 0:
        k = l/2 - 1

def isPalindrome(n):
    nstr = str(n)
    return nstr[-1] != '0' and nstr==nstr[::-1]

def isRootPalindrome(n):
    sqr = n*n
    return isPalindrome(sqr)
    
def listPalin(k):
    result = []
    for i in xrange(1, k):
        istr = str(i)
        p1 = int(istr + istr[::-1])
        p2 = int(istr + istr[-2::-1])
        if p1 < 10000000 and isRootPalindrome(p1):
            result.append(p1*p1)
        if p2 < 10000000 and isRootPalindrome(p2):
            result.append(p2*p2)
    result.sort()
    return result

def main():
    allPalin = listPalin(10000)
    import sys
    lines = open(sys.argv[1]).readlines()
    for i, l in enumerate(lines):
        if i==0:
            continue
        A, B = map(int, l.split())
        print "Case #%d: %d"  % (i, sum(1 for d in allPalin if A <= d <= B))
main()
        
        

        
