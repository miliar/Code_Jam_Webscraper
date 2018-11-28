import sys, math

N = int(sys.stdin.readline())

def palindrome(s):
    return s == s[::-1]

def handlecase(case):
    A, B = sys.stdin.readline().rstrip().split()
    A, B = int(A), int(B)

    c = 0
    for i in xrange(A, B+1):
        s = str(i)
        if palindrome(s):
            sqrt = math.sqrt(i)
            trunc = math.trunc(sqrt)
            if sqrt == trunc and palindrome(str(trunc)):
                c += 1
    print 'Case #%d: %d' % (case, c)

for x in range(N):
    handlecase(x+1)
