n = int(input())
for i in range(1, n + 1):
    s, k = input().split()
    k = int(k)
    s = [1 if j == '-' else 0 for j in s]
    nsum = s[0]
    ss = [0] * len(s)
    ss[0] = s[0]
    for ii in range(1, len(s) - k + 1):
        ss[ii] = (sum(ss[max(0, ii - k + 1):ii]) + s[ii]) % 2
        nsum += ss[ii]
    for ii in range(len(s) - k + 1):
        if ss[ii]:
            for iii in range(ii, ii + k):
                s[iii] = int(not s[iii])
    if any(ii == 1 for ii in s):
        print("Case #%d: IMPOSSIBLE" % i)
    else:
        print("Case #%d: %d" % (i, nsum))
