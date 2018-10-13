import sys

T = int(sys.stdin.readline())

for i in range(T):
    sMax, s = sys.stdin.readline().split()
    sMax = int(sMax)
    assert len(s) == sMax+1
    total = 0
    added = 0
    for j in range(sMax+1):
        num = int(s[j])
        if total < j:
            added += j - total
            total += j - total
        total += num
    print "Case #%d: %d" % (i+1, added)
