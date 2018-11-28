from math import ceil, floor

numbers = []
def pre_calc():
    for n in xrange(1, 10**7 + 1):
        if is_palindrome(n) and is_palindrome(n ** 2):
            numbers.append(n ** 2)

def is_palindrome2(n):
    s = str(n)
    return s == s[::-1]

def is_palindrome(n):
    s = str(n)
    m = len(s) - 1
    for i in range(len(s) / 2):
        if s[i] != s[m - i]:
            return False
    return True

def solve2(a, b):
    aa = int(ceil(a ** 0.5))
    bb = int(floor(b ** 0.5))
    q = 0
    for n in xrange(aa, bb + 1):
        if is_palindrome(n) and is_palindrome(n ** 2):
            q += 1
    return q

def solve(a, b):
    q = 0
    for n in numbers:
        if a <= n <= b:
            q += 1
    return q

pre_calc()

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        A, B = [int(k) for k in raw_input().split()]
        print 'Case #%d: %s' % (t + 1, solve(A, B))
