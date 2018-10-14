import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    line = sys.stdin.readline()
    s, k = line.split()
    s = [p == '+' for p in s]
    k = int(k)
    c = 0
    for i in xrange(len(s) - k + 1):
        if s[i] == False:
            c += 1
            for j in xrange(k):
                s[i+j] = not s[i+j]

    result = str(c) if all(s) else 'IMPOSSIBLE'
    print("Case #%d: %s" % (t+1, result))
