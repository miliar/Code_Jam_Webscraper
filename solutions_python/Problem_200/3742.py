t = int(raw_input())
ss = []
for _ in range(t):
    ss.append(raw_input())

dec = lambda c: str(int(c)-1)

for ti in range(t):
    s = ss[ti][::-1]
    i = 0
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            s = '9' * (i+1) + dec(s[i+1]) + s[i+2:]
    s = s[::-1]
    if s[0] == '0':
        s = s[1:]
    print "Case #%s: %s" % (ti+1, s)
