import sys

def find(a, num):
    for i in range(len(a)):
        if a[i] >= num:
            return i
    return len(a) - 1

def howmany(ss):
    _, s, p = ss[:3]
    triplets = sorted(ss[3:])
    k = 3 * p - 2
    km = 3 * p - 4

    n = 0
    i = find(triplets, k)
    if (triplets[i] >= k):
        n = len(triplets[i:])
        i -= 1
    while s > 0 and i >= 0 and triplets[i] >= km and triplets[i] > 0:
        s -= 1
        n += 1
        i -= 1
    return n

s = sys.stdin.readlines()[1:]

for i in range(len(s)):
    ss = map(int, s[i].strip().split())
    print 'Case #' + str(i+1) + ':', howmany(ss)
