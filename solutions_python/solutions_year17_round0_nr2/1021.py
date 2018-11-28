t = input()
for cas in xrange(t):
    s = map(int, raw_input())

    n = len(s)
    i, j = 0, 1
    while j < n:
        while j < n and s[i] == s[j]:
            j += 1
        if j == n:
            break
        if s[j] > s[i]:
            i = j
            j = j+1
        else:
            s[i] = s[i]-1
            for k in xrange(i+1, n):
                s[k] = 9
            break
    res = ''.join(map(str, s)).lstrip('0')
    print 'Case #{0}: {1}'.format(cas+1, res)
