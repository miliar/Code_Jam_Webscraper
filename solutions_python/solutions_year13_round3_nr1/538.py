import sys


def solve(text, n):
    out_sets = {}
    i = 0
    wovels = set(['a', 'e', 'i', 'o', 'u'])
    l = len(text)
    cnt = 0

    for i in xrange(len(text) - n + 1):
        found = True

        for j in xrange(i, i + n):
            if j >= l or text[j] in wovels:
                found = False
                break

        if found:
            cnt += 1
            #result += (i + 1) * (l - j)
            for x in range(i + 1):
                for y in range(l - j):
                    out_sets[(i - x, j + y)] = True

    return len(out_sets)

stream = sys.stdin
#stream = open("a-in.txt")
T = int(stream.readline())
for c in range(1, T + 1):
    text, n = stream.readline().split()
    n = int(n)

    print "Case #%d: %d" % (c, solve(text, n))
