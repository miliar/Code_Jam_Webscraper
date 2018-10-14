#!/usr/bin/python

import sys
from bisect import bisect_left, bisect_right

#
# If 1 <= s^2 <= 10^14, 1<=s<=10^7, and if s (and s^2) is a
# palindrome, we have s!=10^7. So s has at most 7 digits, hence it is
# made from a "stem" with at most 3 digits.
#
# Every 1<=n<10^3 gives rise to 11 palindromes with between 2 and 7
# digits. So we just need to test 11000+9 palindromic numbers for
# having a palindromic square. After this, counting p
#
# Obviously, this does not scale to the B <= 10^100 case, since we
# would have to generate around 10^25 palindromes. One can make some
# trivial optimizations. For example, note that s must begin/end
# with 1, 2 or 3 if its square is to be a palindrome as well: If s
# begins/ends with (4;5;6;7;8;9), s^2 begins/ends with
# ([12],6;[23],5;[34],6;[456],9;[678],4;[89],1)
#


fair_square = []

def make_palindromes(n):
    result = []
    s = str(n)
    rev = s[::-1]
    result.append(int(s+rev))
    for d in range(10):
        result.append(int(s+str(d)+rev))
    return result


def is_palindrome(n):
    s = str(n)
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

for x in range(1,10):
    if (is_palindrome(x**2)):
        fair_square.append(x**2)

for n in range(1,10**3):
    for x in make_palindromes(n):
        if is_palindrome(x**2):
            fair_square.append(x**2)
    
fair_square.sort()

if len(sys.argv) > 1: 
    inp = open(sys.argv[1]) 
else: 
    inp = sys.stdin


l = inp.readline()
ncases = int(l)

n = 0
for l in inp:
    n += 1
    l = l.strip()
    A,B = l.split()
    A=int(A)
    B=int(B)
    print "Case #%d: %d" % (n, bisect_right(fair_square, B) - bisect_left(fair_square, A))

assert(n == ncases)
