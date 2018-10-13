import math

def is_palindrome(number):
    numstr = str(number)
    return numstr == numstr[::-1]

cases = int(raw_input())

for case in xrange(cases):
    A, B = map(int, raw_input().split())
    count = 0
    for number in xrange(int(math.ceil(math.sqrt(A))), int(math.sqrt(B))+1):
        if not is_palindrome(number):
            continue
        if not is_palindrome(number**2):
            continue
        count += 1

    print 'Case #%d: %d' % (case+1, count)
