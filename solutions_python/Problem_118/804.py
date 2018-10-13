# task = 'C-sample'
task = 'C-small-attempt0'
#task = 'C-large'

testCaseSpec = '''#A #B'''

import math

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def heronSqrt(n):
    x = (n+1)//2
    s = set([x])    # avoid infinite loop if not int
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in s:
            return False    # n is no square
        s.add(x)
    return x

def solve(A, B):
    y = 0
    for n in range(A, B+1):
        if not isPalindrome(n):  # n is no palindrome
            continue

        x = heronSqrt(n)
        if x is False:  # n in no square
            continue

        if isPalindrome(x):     # all conditions true
            y += 1

    return y



from template import Solver

Solver(task, testCaseSpec, solve).solve()

