T = int(raw_input())
for case in range(1,1+T):
    s = raw_input().split(' ')
    K = int(s[1])
    S = s[0]
    n = 0
    for i in range(0, len(S)-K+1):
        if S[i] == "-":
            n += 1
            s2 = ""
            for t in range(i, i+K): s2 += "+" if S[t] == "-" else "-"
            S = S[:i] + s2 + S[i+K:]
    for i in range(len(S)-K+1, len(S)):
        if S[i] == "-": n = -1
    print "Case #%d: %s" % (case, "IMPOSSIBLE" if n == -1 else str(n))
