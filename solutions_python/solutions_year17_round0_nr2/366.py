def solve():
    n = raw_input().strip()
    ans = ""
    p = '0'
    for i, c in enumerate(n):
        if p <= c:
            ans += c
        else:
            t = len(n) - i
            while ans:
                ans = str(int(ans) - 1)
                if all(ans[i] <= ans[i+1] for i in xrange(len(ans) - 1)):
                    break
                t += 1
                ans = ans[:-1]
            if ans == '0':
                ans = ''
            ans += '9' * t
            break
        p = c
    print ans

T = int(raw_input())
for i in xrange(T):
    print "Case #%d:" % (i + 1),
    solve()
