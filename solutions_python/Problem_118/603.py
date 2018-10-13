#!/usr/bin/python3

from math import sqrt
from sys import argv

def isPalindrome(n):
    """Return whether n is a palindrome
    >>> isPalindrome(1)
    True
    >>> isPalindrome(0)
    True
    >>> isPalindrome(33)
    True
    >>> isPalindrome(10)
    False
    >>> isPalindrome(876545678)
    True
    >>> isPalindrome(273)
    False
    """
    str_n = str(n)
    return list(str_n) == list(reversed(str_n))

def isSquareOfPalindrome(n):
    """Return whether n is the square of a palindrome
    >>> isSquareOfPalindrome(121)
    True
    >>> isSquareOfPalindrome(81)
    True
    >>> isSquareOfPalindrome(80)
    False
    >>> isSquareOfPalindrome(82)
    False
    >>> isSquareOfPalindrome(0)
    True
    >>> isSquareOfPalindrome(1)
    True
    >>> isSquareOfPalindrome(2)
    False
    >>> isSquareOfPalindrome(4)
    True
    """
    s = int(sqrt(n) + 0.5)
    return s * s == n and isPalindrome(s)

def fairAndSquareList(n):
    """Return a list of fair and square numbers between 0 and n inclusive
    >>> fairAndSquareList(0)
    [0]
    >>> fairAndSquareList(1)
    [0, 1]
    >>> fairAndSquareList(3)
    [0, 1]
    >>> fairAndSquareList(4)
    [0, 1, 4]
    >>> fairAndSquareList(120)
    [0, 1, 4, 9]
    >>> fairAndSquareList(121)
    [0, 1, 4, 9, 121]
    >>> fairAndSquareList(400)
    [0, 1, 4, 9, 121]
    """
    result = []
    for i in range(n+1):
        li = list(str(i))
        e = int(''.join(li + list(reversed(li))))
        if e <= n:
            if (isSquareOfPalindrome(e)): result.append(e)
        o = int(''.join(li + list(reversed(li))[1:]))
        if o <= n:
            if (o != e and isSquareOfPalindrome(o)): result.append(o)
        else:
            break
    return result

# The above code creates this table for fair and square numbers
# between 0 and 10^14.
table = [
    0,
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004
]

def interval(a, b):
    """Return the number of fair and square numbers between a and b inclusive
    Preconditions: 0 <= a <= b <= 10^14
    >>> interval(1, 4)
    2
    >>> interval(10, 120)
    0
    >>> interval(100, 1000)
    2
    """
    aIndex, bIndex = None, None
    for i in range(len(table)):
        fs = table[i]
        if aIndex == None and fs >= a: aIndex = i
        if bIndex == None and fs >  b: bIndex = i
    if bIndex == None: bIndex = len(table)
    return bIndex - aIndex

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Google Code Jam I/O
    infile = open(argv[1])
    cases = int(infile.readline())
    for i in range(cases):
        a, b = map(int, infile.readline().split())
        print('Case #{}: {}'.format(i+1, interval(a,b)))
