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
    n, t = [int(x) for x in ifile.readline().split()]
    a = [int(x) for x in ifile.readline().split()]
    a.sort()
    res = 0
    while len(a) > 0:
        res += 1
        if len(a) == 1:
            return res
        if a[-1]+a[0] > t:
            a = a[:-1]
        else:
            a = a[1:-1]
    return res

def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

