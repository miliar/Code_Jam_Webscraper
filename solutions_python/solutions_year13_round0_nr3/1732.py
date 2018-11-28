from math import sqrt, ceil

def is_palindrome(n):
    return str(n) == str(n)[-1::-1]


def palindromes(a, b):
    while not is_palindrome(a) and a <= b:
        a += 1
    while a <= b:
        yield a
        s = str(a)
        if s == '9' * len(s):
            a = 10 ** len(s) + 1
            continue
        if len(s) % 2 == 1:
            if s[len(s) / 2] != '9':
                a += 10 ** (len(s) / 2)
            else:
                a += 10 ** (-1 + len(s) / 2)
                a += 10 ** (len(s) / 2)
        else:
            a += 10 ** (-1 + len(s) / 2)
            a += 10 ** (len(s) / 2)


for t in range(input()):
    print "Case #%s:" % str(t + 1),
    a, b = map(int, raw_input().split())
    n = 0
    for i in palindromes(int(ceil(sqrt(a))), int(sqrt(b))):
        if is_palindrome(i * i):
            n += 1
    print n

