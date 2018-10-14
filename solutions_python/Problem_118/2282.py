'''
Created on Apr 13, 2013

@author: jirasch
'''
import math

def is_palindrome(x):
    x = str(x)
    if x[::-1] == x:
        return True
    return False

def is_fair_square(x):
    return is_palindrome(x) and is_palindrome(x * x)

def solve(case):
    a, b = [int(x) for x in case.split(' ')]
    count = 0
    base_a = int(math.ceil(math.sqrt(a)))
    base_b = int(math.floor(math.sqrt(b)))
    for x in range(base_a, base_b+1):
        if is_fair_square(x):
            count += 1
    return count

afile = file('c-small-attempt0.in')
lines = afile.read().splitlines()
afile.close()

num = int(lines[0].strip())
cases = [lines[i+1] for i in range(num)]

i = 1
for c in cases:
    print 'Case #%d: %s' % (i, solve(c))
    i += 1
