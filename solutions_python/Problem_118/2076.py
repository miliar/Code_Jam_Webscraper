import math

def isSquare(n):
    return math.floor(math.sqrt(n))**2 == n

def isPalindrome(s):
    return s == s[::-1]

def countFairSquare(a, b):
    count = 0
    for i in range(a, b+1):
        if isSquare(i) and isPalindrome(str(i)) and isPalindrome(str(int(math.sqrt(i)))):
            count += 1
    return count

if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        A, B = map(int, (f.readline().strip().split()))
        count = countFairSquare(A, B)
        print 'Case #%d: %d'%(i+1, count)



