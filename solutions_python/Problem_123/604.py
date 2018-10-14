T = input()

for case in xrange(1, T+1):
    A, n = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()

    if A == 1 and a[0] >= 1:
        print 'Case #{case}: {ans}'.format(case=case, ans=n)
        continue

    ans = 0
    for i in xrange(n):
        m, t = 0, A
        while t <= a[i]:
            m += 1
            t += t-1
        if m < n-i:
            A = t + a[i]
            ans += m
        else:
            ans += n-i
            break
    print 'Case #{case}: {ans}'.format(case=case, ans=ans)

