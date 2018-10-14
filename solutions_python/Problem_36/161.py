file = open("C-large.in")
lines = int(file.next())
s = 'welcome to code jam'
kmax = len(s)
for i in range(lines):
    t = file.next().strip()
    jmax = len(t)
    m = [[0 for j in range(jmax+1)] for k in range(kmax)]
    for j in range(1, jmax+1):
        if s[0] == t[j - 1]:
            m[0][j] = m[0][j - 1] + 1
        else:
            m[0][j] = m[0][j - 1]
    for k in range(1, kmax):
        for j in range(1, jmax+1):
            if s[k] == t[j - 1]:
                m[k][j] = m[k-1][j] + m[k][j-1]
            else:
                m[k][j] = m[k][j-1]
    print "Case #%i: %.4i" % (i + 1, m[kmax-1][jmax] % 10000)
