
from sys import stdin


def is_palindrome(n):
    forward = str(n)
    backward = [c for c in forward]
    backward.reverse()
    backward = ''.join(backward)
    return forward == backward

cases = int(stdin.readline())

for case in range(1, cases+1):
    (A, B) = [int(n) for n in stdin.readline().split()]
    
    fairsquare = 0
    current = int(A**0.5) if A >= 0 else 0
    square = current * current

    while square <= B:
        if square >= A and is_palindrome(current) and is_palindrome(square):
            fairsquare += 1
            #print "%s is fair and square" % square
        current += 1
        square = current * current

    print "Case #%s: %s" % (case, fairsquare)
