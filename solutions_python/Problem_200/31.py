import sys

T = int(raw_input())

def fix(x):
    k = map(int, str(x))
    res = k[0]
    lower_flag = False
    for idx in xrange(1, len(k)):
        if k[idx] < k[idx-1]:
            lower_flag = True
        if lower_flag:
            k[idx] = k[idx - 1]
        res = res * 10 + k[idx]

    return res

def check_inc(x):
    s = str(x)
    for idx in xrange(1, len(s)):
        if s[idx] < s[idx - 1]:
            return False
    return True

def solve(n):
    l = 1
    r = n
    while l < r:
        m = (l + r + 1) / 2
        t = fix(m)
        if t <= n:
            l = m
        else:
            r = m - 1
    return l

def naive_solve(n):
    ans = 0
    for i in range(1, n + 1):
        if check_inc(i):
           ans = i
    return ans

cnt = 0
for line in sys.stdin:
    cnt += 1
    if cnt > T:
        break
#    assert solve(int(line)) == naive_solve(int(line))
    print "Case #%s: %s" % (cnt, solve(int(line)))
