import math

def isFair(n):
    nstr = str(n)
    nlen = len(nstr)

    for i in xrange(0, nlen / 2):
        if nstr[i] != nstr[nlen-i-1]:
            return False

    return True

def isFairSquare(n):
    if isFair(n):
        if isFair(n*n):
            return True

    return False

def nbFairSquare(a, b):
    sqA, sqB = int(math.ceil(math.sqrt(a))), int(math.sqrt(b))

    nb = 0
    for i in xrange(sqA, sqB+1):
        if isFairSquare(i):
            nb += 1

    return nb

if __name__ == '__main__':
    size = int(raw_input())
    for i in xrange(0, size):
        a, b = [int(_) for _ in raw_input().split()]
        print "Case #" + str(i+1) + ": " + str(nbFairSquare(a, b))
