t = input()
for i in range(t):
    smax, s = raw_input().split()
    smax = int(smax)
    ans = 0
    count = 0
    for j in range(len(s)):
        # print j, count, ans
        if count < j:
            ans += j - count
            count += j - count
        count += int(s[j])
        # print j, count, ans
    print 'Case #{0}: {1}'.format(i + 1, ans)