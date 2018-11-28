import math

def pal(n): # O(3n)
    s = str(n) # O(n)
    return s == s[::-1] # O(2n)

num_cases = int(raw_input())
for case in xrange(1, num_cases + 1):
    lo, hi = map(int, raw_input().split())
    lo, hi = int(math.ceil(math.sqrt(lo))), int(math.sqrt(hi))
    num_pals = 0
    for n in xrange(lo, hi + 1):
        if pal(n) and pal(n * n):
            num_pals += 1
    print "Case #%d: %d" % (case, num_pals)
