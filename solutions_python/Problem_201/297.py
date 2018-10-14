
from collections import defaultdict

def calculate(n, ka):
    buf = {n: 1}
    left = ka
    while True:
        s = sum(buf.values())
        if left <= s:
            k = sorted(buf.keys())[-1]
            if left > buf[k]:
                k = sorted(buf.keys())[0]
            vals = [(k-1)/2, k-1-(k-1)/2]
            vals.sort()
            vals.reverse()
            return vals
        left -= s
        new_buf = defaultdict(int)
        for k in buf.keys():
            k1 = (k-1)/2
            k2 = k-1-k1
            new_buf[k1] += buf[k]
            new_buf[k2] += buf[k]
        buf = new_buf

cases = int(raw_input())
for i in xrange(1, cases+1):
    n, k = map(int, raw_input().split(' '))
    mx, mi = calculate(n, k)
    print "Case #%d: %d %d" % (i, mx, mi)


