def is_tidy(n):
    strn = str(n)
    for i in range(1, len(strn)):
        if strn[i - 1] > strn[i]:
            return False
    return True

with open('/Users/girishkadli/Desktop/codejam/test.txt', 'r') as f:
    lines = f.readlines()
    t = int(lines[0])
    for i in range(1, t + 1):
        k = int(lines[i])
        ans = k
        for j in range(k, 1, -1):
            if is_tidy(j):
               ans = j
               break

        print 'Case #%s: %s' % (str(i), str(ans))
