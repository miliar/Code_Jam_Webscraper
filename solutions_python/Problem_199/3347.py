t = int(raw_input())
sk = []
for _ in range(t):
    s,k = raw_input().split()
    s = [1 if c == '+' else 0 for c in s]
    k = int(k)
    sk.append((s,k))

flip = lambda a: map(lambda x: 1-x, a)

for ti in range(t):
    s,k = sk[ti]
    i = 0
    c = 0
    while i < len(s) - k+1:
        if s[i] == 1:
            i += 1
        elif s[i:i+k] == [0]*k:
            s = s[:i] + [1]*k + s[i+k:]
            c += 1
            i += k
        else:
            s = s[:i] + flip(s[i:i+k]) + s[i+k:]
            c += 1
            i += 1
    if all(s[i:]):
        print "Case #%s: %s" % (ti+1, c)
    else:
        print "Case #%s: IMPOSSIBLE" % (ti+1)
