from sys import *

inp = open("text.in", "r")
out = open("text.out", "w")

def go(c1, c2):
    if c1 == '1':
        if c2 == '1':
            return ['1', 1]
        if c2 == 'i':
            return ['i', 1]
        if c2 == 'j':
            return ['j', 1]
        if c2 == 'k':
            return ['k', 1]
    if c1 == 'i':
        if c2 == '1':
            return ['i', 1]
        if c2 == 'i':
            return ['1', -1]
        if c2 == 'j':
            return ['k', 1]
        if c2 == 'k':
            return ['j', -1]
    if c1 == 'j':
        if c2 == '1':
            return ['j', 1]
        if c2 == 'i':
            return ['k', -1]
        if c2 == 'j':
            return ['1', -1]
        if c2 == 'k':
            return ['i', 1]
    if c1 == 'k':
        if c2 == '1':
            return ['k', 1]
        if c2 == 'i':
            return ['j', 1]
        if c2 == 'j':
            return ['i', -1]
        if c2 == 'k':
            return ['1', -1]


tests = int(inp.readline())
for test in range(tests):
    l, x = inp.readline().split()
    l = int(l)
    x = int(x)
    s = inp.readline().strip()
    s = s * x
    out.write('Case #%d: ' % (test + 1))
    sign = 1
    now = s[0]
    suff = ['' for i in range(len(s))]
    suff[len(s) - 1] = s[-1]
    suffsign = [1 for i in range(len(s))]
    for i in range(len(s) - 2, -1, -1):
        suff[i] = go(s[i], suff[i + 1])[0]
        suffsign[i] = suffsign[i + 1] * go(s[i], suff[i + 1])[1]
    havek = [False for i in range(len(s))]
    havek[len(s) - 1] = (suff[len(s) - 1] == 'k') and (suffsign[len(s) - 1] == 1)
    for i in range(len(s) - 2, -1, -1):
        havek[i] = havek[i + 1] or ((suff[i] == 'k') and (suffsign[i] == 1))
    ok = False
    for i in range(len(s) - 2):
        if (now == 'i') and (sign == 1) and (suff[i + 1] == 'i') and (suffsign[i + 1] == 1):
            if havek[i + 2]:    
                ok = True
        tmp = go(now, s[i + 1])
        now = tmp[0]
        sign *= tmp[1]
    out.write(("YES" if ok else "NO") + '\n')