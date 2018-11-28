cases = int(raw_input())

def recycle(n, A, B):
    digits = list(str(n).lstrip("0"))
    r = set()
    for i in xrange(len(digits)):
        m = int("".join(digits[i:]+digits[:i]))
        if A <= n and n < m and m <= B:
            r.add(m)
    return r

for case in xrange(cases):
    A, B = [int(x) for x in raw_input().split()]
    total = 0
    for n in xrange(A, B+1):
        r = recycle(n,A,B)
        total += len(r)
    print "Case #%d: %d" % (case+1, total)
