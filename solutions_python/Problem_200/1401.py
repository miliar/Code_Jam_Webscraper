def nearest(s):
    s = [int(x) for x in s]
    b = 0
    i = 1
    while i < len(s):
        if s[b] < s[i]:
            b = i
        elif s[b] > s[i]:
            s[b] -= 1
            for j in xrange(b+1, len(s)):
                s[j] = 9
        i += 1
    return ''.join(str(x) for x in s).lstrip('0')

t = int(raw_input())
for kei in xrange(1, t+1):
    s = raw_input()
    print "Case #{}: {}".format(kei, s if len(s) == 1 else nearest(s))