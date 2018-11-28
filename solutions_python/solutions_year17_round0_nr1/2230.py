test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    s = raw_input().split()
    k = int(s[1])
    s = list(s[0])
    c = 0
    for i in xrange(0, len(s) - k + 1):
        if s[i] == '-':
            for j in xrange(i,  i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
            c += 1

    b = True
    for i in xrange(len(s) - k, len(s)):
        if s[i] == '-':
            b = False
    if b:
        print "Case #{}: {}".format(case, c)
    else:
        print "Case #{}: {}".format(case, "IMPOSSIBLE")