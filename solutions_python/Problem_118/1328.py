import string
import itertools
from math import ceil


def get_palindroms(a=0, int=int, str=str):
    "Return a list of all palindrom numbers greater than a."
    odd_fmt = "{0}{1}{2}".format
    even_fmt = "{0}{1}".format
    if a < 10:
        for i in range(a, 10): yield i
        i = 1
        odd = False
        s = 1
    else:
        a_str = str(a)
        s = len(a_str)
        odd = s % 2
        i = int(a_str[:s/2])
    while 1:
        r = str(i)[::-1]
        if odd:
            for d in string.digits:
                n = int(odd_fmt(i, d, r))
                if n >= a:
                    yield n
        else:
            n = int(even_fmt(i, r))
            if n >= a:
                yield n
        if i == int('9' * s):
            odd = not odd
            if not odd:
                i += 1
                s += 1
            else:
                i -= int('8' + '9' * (s-1))
        else:
            i += 1


def ispalindrom(n, str=str):
    return str(n) == str(n)[::-1]


def solve(a, b):
    res = 0
    palindroms = get_palindroms(int(ceil(a**.5)))
    for n in  itertools.takewhile(lambda x: x <= b**0.5, palindroms):
        if ispalindrom(n**2):
            #print n**2
            res += 1
    return res


def main():
    t = int(raw_input())
    for i in range(t):
        a, b = map(int, raw_input().split())
        res = solve(a, b)
        print "Case #%d: %d" % (i + 1, res)


if __name__ == "__main__":
    main()
    #print list(itertools.takewhile(lambda x: x <= 2002, get_palindroms(1991)))
