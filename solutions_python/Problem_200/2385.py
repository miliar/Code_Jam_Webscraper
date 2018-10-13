test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    s = list(raw_input().rstrip())
    i = 0
    r = ['0']*len(s)
    k = -1
    while i < len(s) - 1 and s[i] <= s[i + 1]:
        if s[i] == s[i + 1]:
            if k == -1:
                k = i
        else:
            k = -1
        r[i] = s[i]
        i += 1

    if i == len(s) - 1:
        r[i] = s[i]
    else:
        if k != -1:
            i = k
        r[i] = chr(ord(s[i][0]) - 1)
        i += 1
        for j in xrange(i, len(s)):
            r[j] = '9'
    print "Case #{}: {}".format(case, int(''.join(r)))
