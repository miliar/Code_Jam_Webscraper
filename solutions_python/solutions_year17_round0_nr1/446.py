import sys

def foo3(n):
    res = 0
    while n > 0:
        res += n % 2
        n //= 2
    return res

def foo2(a, b, n):
    n2 = n
    i = 0
    while n > 0:
        if n % 2 == 1:
            for i2 in range(len(a)):
                a[i2][i] = chr(97-ord(a[i2][i]))
        n //= 2
        i += 1
    a.sort()
    if a == b:
        return foo3(n2)
    return 1000


def foo(ifile):
    s, n = ifile.readline().split()
    n = int(n)
    a = [0] * len(s)
    for i in range(len(s)):
        if s[i] == '+':
            a[i] = 1

    res = 0
    for i in range(len(s)):
        if a[i] == 1:
            continue
        if i + n > len(s):
            return 'IMPOSSIBLE'
        res += 1
        for j in range(i, i+n):
            a[j] = 1 - a[j]

    return res

def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

