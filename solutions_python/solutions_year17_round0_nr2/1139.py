# -*- coding: utf-8 -*-

def solve(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            s2 = s[:i] + str(int(s[i])-1) + '9'*(len(s)-i-1) 
            #print(s2)
            return solve( s2 )
    return s


f = open('B-large.in','r')
fo = open('result.txt','w')
t = int(f.readline())
for ti in range(t):
    s = f.readline()[:-1]
    r = int(solve(s))
    rs = "Case #%d: %d\n" % (ti+1, r)
    print(rs)
    fo.write( rs )
fo.close()
f.close()