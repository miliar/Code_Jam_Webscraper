def flip(s):
    return s.replace("-", ".").replace("+", "-").replace(".", "+")

def go(s, k, lastflipped = -1):
    if all(c == "+" for c in s):
        return 0
    if (s, lastflipped) in v:
        return v[(s, lastflipped)]
    m = 9999999999
    for i in range(lastflipped + 1, len(s) - k + 1):
        s2 = s[:i] + flip(s[i:i+k]) + s[i+k:]
        t = go(s2, k, i)
        if (t >= 0):
            m = min(m, 1 + t)
    if m <= 99999999:
        return v.setdefault((s, lastflipped), m)
    return v.setdefault((s, lastflipped), -1)

for q in range(1, input() + 1):
    v = {}
    s, k = raw_input().split()
    k = int(k)
    t = go(s, k)
    if t == -1:
        print "Case #%s: %s" % (q, "IMPOSSIBLE")
    else:
        print "Case #%s: %s" % (q, t)


