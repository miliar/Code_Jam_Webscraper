def is_palindrome(num):
    rev = 0
    orig = num
    while num > 0:
        rev = rev * 10 + num % 10
        num /= 10
    return orig == rev

from math import sqrt,ceil
import sys

def is_fair(sqrt_of_num):
    if not is_palindrome(sqrt_of_num):
        return False
    else:
        return is_palindrome(sqrt_of_num * sqrt_of_num)

case_list = []
case_res = []
first = True
small = 10**100
big = 0
for line in sys.stdin:
    if first:
        first = False
        continue # skip first line in hax
    a,b = line.split()
    a = int(a)
    b = int(b)
    case_list.append( (a,b) )
    case_res.append(0)
    small = min(small, a)
    big = max(big, b)

small = int(ceil(sqrt(small)))
big = int(ceil(sqrt(big)))

for i in xrange(small, big+1):
    if is_palindrome(i):
        s = i * i
        if is_palindrome(s):
            for n, (a,b) in enumerate(case_list):
                if s >= a and s <= b:
                    case_res[n] += 1

for n, res in enumerate(case_res):
    print "Case #%d: %d" % (n+1, res)
