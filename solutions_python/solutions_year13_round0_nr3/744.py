import sys
import math


def getline():
    return sys.stdin.readline().strip()


getints = lambda: map(int, getline().split(' '))


def is_palindrome(num):
    s = str(num)
    slen = len(s)
    for i in xrange(slen / 2):
        if s[i] != s[slen - i - 1]:
            return False
    return True

squares = []
base = 0
max_sq = 10**14
while True:
    if is_palindrome(base):
        sq = base ** 2
        if sq > max_sq:
            break
        if is_palindrome(sq):
            squares.append(sq)
    base += 1 

cases, = getints()

for case in xrange(cases):
    a, b = getints()

    num_fair_square = 0

    for sq in squares:
        if sq < a:
            continue
        if sq > b:
            break
        num_fair_square += 1

    print "Case #{case}: {result}".format(case=case + 1, result=num_fair_square)
