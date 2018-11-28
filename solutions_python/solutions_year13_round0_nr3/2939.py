import math
import sys
sys.stdin = open('C-small-attempt0.in')
sys.stdout = open('out.txt', 'w')

def check(s):
    s = str(s)
    s1 = s[::-1]
    if s == s1:
        return 1
    else:
        return 0

def fun(l, r):
    cnt = 0
    ll = int(math.sqrt(l))
    rr = int(math.sqrt(r))
    for i in xrange(ll, rr + 1):
        if check(i) == 1:
            tmp = i ** 2
            if l <= tmp <= r and  check(tmp) == 1:
                cnt += 1
              #  print tmp
    return cnt
    
T = input()
for i in xrange(1, T + 1):
    l, r = map(int, raw_input().split())
    print "Case #%d: %d\n" % (i, fun(l, r))
    
