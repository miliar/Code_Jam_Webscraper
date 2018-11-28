def last_tidy(n):
    if n < 10:
        return n
    s = str(n)
    for i in range(len(s) - 2, -1, - 1):
        if int(s[i]) > int(s[i + 1]):
            s = s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1)
    return int(s)


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print "Case #%d: %d" % (i + 1, last_tidy(n))
