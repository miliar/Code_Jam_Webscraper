import sys
import math

T = int(sys.stdin.readline())

def isPalindrome(x):
    return `x`==`x`[::-1]

def isSquare(x):
    return math.sqrt(x).is_integer()


for case in xrange(T):
    A, B = sys.stdin.readline().strip().split()

    A = int(A)
    B = int(B)

    num = 0

    for x in xrange(A, B+1):
        if isPalindrome(x) and isSquare(x) and isPalindrome(int(math.sqrt(x))):
            num = num + 1

    print "Case #%d: %d" % (case+1, num)