#!python
import sys

def gets():
    return sys.stdin.readline().rstrip('\r\n')

def readint():
    return int(gets())

def readints():
    return [int(i) for i in gets().split()]

def is_palin(x):
    s = str(x)
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# fair and square numbers
fsn = []
for i in xrange(10**7+1):
    if is_palin(i):
        i2 = i**2
        if is_palin(i2):
            fsn.append(i2)
        if i2 > 10**14:
            break


T = readint()
for nCase in xrange(T):
    a, b = readints()
    ans = 0
    for i in fsn:
        if i >= a and i <= b:
            ans += 1
    print("Case #%d: %d" % (nCase+1, ans))
