

def check(s, p, l):
    for i in xrange(l):
        if p[i] != '?' and p[i] != s[i]:
            return False
    return True


def solve(t):
    C, J = raw_input().split()
    l = len(C)
    ans = []

    for n in xrange(10**l):
        ns = str(n)
        while len(ns) < l:
            ns = '0' + ns
        if not check(ns, C, l):
            continue

        for m in xrange(10**l):
            ms = str(m)
            while len(ms) < l:
                ms = '0' + ms
            if not check(ms, J, l):
                continue
            ans.append((abs(n-m), n, m, ns, ms))

    ans.sort()
    c, j = ans[0][3], ans[0][4]
    print 'Case #%d: %s %s' % (t, c, j)


T = input()
for i in xrange(T):
    solve(i+1)
