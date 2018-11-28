from sys import stdin
from math import floor, ceil, sqrt, log10
from pylab import zeros, uint8, flipud, r_, arange

def parse():
    return tuple(int(x) for x in stdin.readline()[:-1].split(' '))

def solve(low, high):
    lows, highs = sqrt(low), sqrt(high)
    digsl, digsh = digs(lows), digs(highs)
    count = 0
    for digits in xrange(digsl, digsh + 1):
        count += solveDigit(digits, lows, highs)
    return str(count)

def solveDigit(digits, min, max):
    half = int(ceil(digits / 2.))
    count = 0
    for test in xrange(10 ** (half - 1), 10 ** half):
        pal = makePalindrome(test, digits % 2 == 0)
        if pal >= min and pal <= max and isPalindrome(pal ** 2):
            count += 1
    return count

def digs(num):
    return int(floor(log10(num))) + 1

def decomp(num):
    digits = digs(num)
    arr = zeros(digits, dtype=uint8)
    for i in xrange(digits):
        arr[i] = num % 10
        num /= 10
    return arr

def fuse(arr):
    return arr.dot(10 ** arange(arr.size))

def makePalindrome(num, even):
    dec = decomp(num)
    if even:
        return fuse(r_[dec, flipud(dec)])
    else:
        return fuse(r_[dec, flipud(dec[:-1])])

def isPalindrome(num):
    arr = decomp(num)
    for i in xrange(arr.size / 2):
        if arr[i] != arr[arr.size - i - 1]:
            return False
    return True

if __name__ == '__main__':
    T = int(stdin.readline())
    for i in xrange(T):
        print 'Case #' + str(i + 1) + ':', solve(*parse())
