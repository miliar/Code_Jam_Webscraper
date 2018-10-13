# Andy Rock
# April 7, 2016
# 
# Qualification Round 2017: Problem A. 

for T in xrange(1, int(raw_input()) + 1):
    s, k = raw_input().split()
    s = [t for t in s]
    k = int(k)

    ans = 0
    for i in xrange(len(s) - k + 1):
        if s[i] == '-':
            ans += 1
            for j in xrange(i, i + k):
                s[j] = '+' if s[j] == '-' else '-'

    if s != ['+'] * len(s):
        ans = "IMPOSSIBLE"
    print 'Case #%d: %s' % (T, ans)
