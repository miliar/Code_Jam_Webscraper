def f(s):
    p = -1
    for i in range(len(s)):
        m = -1
        g = ""
        for j in range(len(s)):
            if j <= i:
                g += s[j]
                m = max(m, int(s[j]) - int('0'))
            else:
                g += str(m)
        m = -1
        ok = True
        for j in range(len(g)):
            if int(g[j]) - int('0') < m:
                ok = False
                break
            m = max(m, int(g[j]) - int('0'))
        if ok == True and g <= s:
            p = i
    res = ""
    if p == -1:
        if s[0] != '1':
            res += str(int(s[0]) - 1)
        for i in range(1, len(s)):
            res += '9'
    else:
        for i in range(p + 1):
            res += s[i]
        if p + 1 < len(s):
            res += str(int(s[p + 1]) - 1)
        while len(res) < len(s):
            res += '9'
    return res

T = int(raw_input())

for t in range(T):
    s = raw_input()
    print "Case #" + str(t + 1) + ": " + f(s)
