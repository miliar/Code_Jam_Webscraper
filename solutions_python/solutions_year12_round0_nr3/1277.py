import sys

def rec(m, A, B):
    count = 0
    s = str(m)
    prev = []
    for i in range(1, len(s)):
        ns = s[i:] + s[:i]
        n = int(ns)
        if n < m and n >= A and n <= B and len(ns) == len(s) and n not in prev:
            prev.append(n)
            count += 1
    return count


cases = int(sys.stdin.readline())

for case in range(1, cases + 1):
    A, B = [int(x) for x in sys.stdin.readline().split()]
    print "Case #%d: %d" % (case, sum([rec(m, A, B) for m in range(A, B + 1)]))
