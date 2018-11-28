import sys
def count(MIN, MAX):

    s = set()
    L = len(str(MAX))
    for i in xrange(MIN, MAX + 1):
        for j in xrange(1, L):
            div = 10**j
            h = i / div
            l = i % div
            n = l * 10 ** (L - j) + h
            if i != n and i < n and n <= MAX and (l * 10 / div) != 0:
    #            print i, h, l, n, l * 10 / div
                s.add((i, n))

    return len(s)

#print count(1, 9)
#print count(10, 40)
#print count(100, 500)
#print count(1111, 2222)
#print count(1, 2000000)

N = sys.stdin.readline()
i = 0
for l in sys.stdin:
    i += 1
    min, max = l.split()
    print "Case #{0}: {1}".format(i, count(int(min), int(max)))

