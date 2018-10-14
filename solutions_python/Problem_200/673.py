n = int(raw_input())
for i in xrange(n):
    s = raw_input()
    if "".join(sorted(s)) == s:
        print "Case #{0}: {1}".format(i + 1, s)
        continue

    best = int("9" * (len(s) - 1))
    for j in xrange(len(s)):
        if s[j] != '0':
            t = s[:j] + str(int(s[j]) - 1) + ("9" * (len(s) - 1 - j))
            if "".join(sorted(t)) == t and int(t) > best:
                best = int(t)

    print "Case #{0}: {1}".format(i + 1, best)
