import sys

def addMin(level, stoodup):
    x = level - stoodup
    return x
"""
    cnt = 0
    while cnt + stoodup < level:
        cnt += 1
    assert x == cnt
    return cnt
"""

for tc in range(1, 1 + int(sys.stdin.readline())):
    line = sys.stdin.readline()
    smax, vals = line.split(" ")
    smax = int(smax)
    #print smax, vals
    stoodup = 0
    s = 0
    required = 0
    counts = vals.strip()
    level = 0
    for count in counts:
        if stoodup >= level:
            #print "OK"
            stoodup += int(count)
        else:
            #print "not enough"
            cnt = addMin(level, stoodup)
            required += cnt
            #print "addMin(%d,%d)=%d" % (level, stoodup, cnt)
            stoodup += cnt + int(count)
        level += 1
    print "Case #%d: %d" % (tc, required)

