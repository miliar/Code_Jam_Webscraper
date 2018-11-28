import sys
from math import ceil, floor, sqrt

def is_palindrome(x):
    x = str(x)
    y = x[::-1]
    return x == y

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    (A, B) = [int(x) for x in f.readline().split()]
    (a, b) = (int(ceil(sqrt(A))), int(floor(sqrt(B))))

    count = 0
    for x in range(a, b + 1):
        if is_palindrome(x) and is_palindrome(x*x):
            count += 1

    print "Case #%d: %d" % (case + 1, count)
