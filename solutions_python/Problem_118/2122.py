#!/usr/bin/env python
import sys


chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def doit(a, b):
    palindromes = []
    count = 0
    for i in range(b+1):
        if isPalindrome(i):
            palindromes += [i]

    for p in palindromes:
        square = p*p
        if square >= a and square <= b and isPalindrome(square):
            count += 1

    return count


def make():
    work = chars[0]


    palindrome = makePalindrome(work)


def step(work):
    t = len(work)-1
    while True:
        i = chars.index(work[t])
        #print 'i', i, 'len chars', len(chars), 't', t

        if i == len(chars)-1:
            if t == 0:
                return work + chars[0]
            work = stringSet(work, t, chars[0])
            t -= 1
            continue
        else:
            work = stringSet(work, t, chars[i+1])
        return work


def stringSet(work, index, replace):
    #print 'setString', work, index, replace
    return work[:index] + replace + work[index+1:]


def makePalindrome(half):
    return half + half[::-1]


def isPalindrome(x):
    x = str(x)
    return x == x[::-1]


if __name__ == '__main__':
    assert isPalindrome(6) is True
    assert isPalindrome(11) is True
    assert isPalindrome(121) is True

    assert isPalindrome(12) is False
    assert isPalindrome(223) is False
    assert isPalindrome(2244) is False

    assert doit(1, 4) is 2
    assert doit(1, 1) is 1
    assert doit(10, 120) is 0
    assert doit(100, 1000) is 2

    assert stringSet("0", 0, "1") == '1'
    assert stringSet("012", 2, "3") == '013'
    assert step('0') == '1'
    assert step('01') == '02'
    assert step('09') == '10'


if __name__ == '__main__' and True:
    cases = int(sys.stdin.readline())
    for case in xrange(1, cases+1, 1):
        x = map(int, sys.stdin.readline().split())
        print "Case #%d: %d" % (case, doit(x[0], x[1]))
