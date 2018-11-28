
def is_ok(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False



numbers = []
for num in xrange(1, 100001):
    if is_ok(num):
        numbers.append(num)
import math
t = int(raw_input()) + 1
for kase in xrange(1, t):
    ans = 0
    a, b = map(int, raw_input().split())
    for i in xrange(a, b + 1):
        t = math.sqrt(i)
        if t * t == i and t in numbers and i in numbers:
            ans += 1
    print "Case #%s: %s" % (kase, ans)
