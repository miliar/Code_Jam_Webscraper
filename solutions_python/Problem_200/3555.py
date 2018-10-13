#!/usr/bin/python

t = int(raw_input())
def check(s):
    ok = True
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            ok = False
    return ok
for tc in range(1,t+1):
    s = raw_input()
    sn = int(s)
    ans = sn
    if len(s) > 1:
        ok = check(s)
        if ok:
            ans = sn
        else:
            ans = int('9'*(len(s)-1))
            for i in range(1,len(s)):
                t1 = s[:i]
                t2 = s[i:]
                r1 = str(int(t1)-1)
                r2 = '9'*(len(t2))
                temp = int(r1+r2)
                if check(str(temp)) and temp < sn:
                    if ans == -1 or ans < temp:
                        ans = temp
    print 'Case #%d: %d'%(tc,ans)
