T = int(raw_input())
for t in xrange(1, T+1):
    N = raw_input()
    n = int(N)
    if n < int('1' * len(N)):
        print 'Case #%d: %s' % (t, '9' * (len(N) - 1))
        continue
    ans = [int(N[0])]
    for i in xrange(1, len(N)):
        if int(N[i]) < ans[i-1]:
            ans[i-1] -= 1
            for j in xrange(i-2, -1, -1):
                if ans[j] > ans[j+1]:
                    ans[j] -= 1
                    ans[j+1] = 9
            for k in xrange(i, len(N)):
                ans.append(9)
            break
        else:
            ans.append(int(N[i]))
    print 'Case #%d: %s' % (t, ''.join(map(str, ans)))

