from math import sqrt

def palindrome(s):
    l = len(s)
    if l == 1:
        return True
    m = l/2
    n = m - 1 + l % 2
    return s[:m] == s[-1:n:-1]

def c(low, high):
    total = 0
    for i in xrange(low, high+1):
        if palindrome(str(i)):
            root2 = sqrt(i)
            if root2 == int(root2) and palindrome(str(int(root2))):
                total += 1
    return total

if __name__ == '__main__':
    import sys
    cases = int(sys.stdin.readline())
    for tc in range(1, cases+1):
        A, B = map(int, sys.stdin.readline().split())
        print 'Case #{0}: {1}'.format(tc, c(A,B))
