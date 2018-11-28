import math

f = open('C-small-attempt0.in')
raw_input = f.readline

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

def is_square(n):
    return math.sqrt(n).is_integer()

testcases = int(raw_input())

for i in range(testcases):
    start, end = [int(k) for k in raw_input().split()]
    result = 0
    for j in range(start, end + 1):
        if is_palindrome(j) and is_square(j) and is_palindrome(int(math.sqrt(j))):
            result += 1
    print 'Case #{0}: {1}'.format(i + 1, result)
