#!/usr/bin/python

def num2list(n):
    L = []
    while n > 0:
        L.append(n % 10)
        n = n / 10
    L.reverse()
    return L

def list2num(L):
    LL = L[:]
    LL.reverse()
    pow10 = 1
    n = 0
    for digit in LL:
        n += pow10 * digit
        pow10 *= 10
    return n

def tidy(L):
    if len(L) <= 1:
        return L
    leading_digit = L[0]
    assert leading_digit >= 0 and leading_digit < 10
    if [leading_digit] * len(L) <= L:
        return [leading_digit] + tidy(L[1:])
    else:
        if leading_digit > 0:
            return [leading_digit - 1] + [9] * (len(L) - 1)
        else:
            assert(False)

def tidy_int(n):
    L = num2list(n)
    tL = tidy(L)
    t = list2num(tL)
    return t

num_lines = int(raw_input())
for i in xrange(num_lines):
    n = int(raw_input())
    print "Case #%d: %d" % (i+1, tidy_int(n))
