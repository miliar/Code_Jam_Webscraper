import sys
import heapq
import collections

def foo2(x):
    if x % 2 == 1:
        return "%s %s" % (x//2, x//2)
    else:
        return "%s %s" % (x//2, x//2-1)


def foo(ifile):
    n, k = [int(x) for x in ifile.readline().split()]
    a = {n:1}

    while k > 0:
        x = max(a.keys())
        if a[x] >= k:
            return foo2(x)
        k -= a[x]
        if x % 2 == 1:
            a[x//2] = a.get(x//2, 0) + a[x]*2
        else:
            a[x//2] = a.get(x//2, 0) + a[x]
            a[x//2-1] = a.get(x//2-1, 0) + a[x]
        del a[x]





def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

