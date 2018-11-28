import sys

def solve(c):
    print 'Case #%d:' % c,
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    m = len(s)
    n = len(t)
    i = j = actions = 0
    f = False

    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if s[i-1] == t[j]:
                j += 1
                actions += 1
            elif t[j-1] == s[i]:
                i += 1
                actions += 1
            else:
                f = True
                break
    if not f:
        while i < m:
            if s[i] != t[-1]:
                f = True
                break
            i +=1
            actions += 1

        while j < n:
            if t[j] != s[-1]:
                f = True
                break
            j +=1
            actions += 1

    if f:
        print 'Fegla Won'
    else:
        print actions

N = int(sys.stdin.readline())
for c in xrange(1, N+1):
    solve(c)
