'''
Created on Apr 13, 2013

@author: Saravanan V
'''

import math

def pal(p):
    s1 = str(p)
    s2 = s1[::-1]
    return s1 == s2
def sqrt_of_pal(n):
    sq= math.sqrt(n)
    if str(sq-long(sq))[1:] == '.0':
        return pal(long(sq))
    else:
        return False
        
with open('input.in') as f:
    lines = f.readlines()
with open('output.out', 'w') as output:
    N = int(lines[0])
    c=1
    for tc in range(N):
        l1 = lines[c].strip()
        c = c+1
        s = l1.split()
        tot=0
        for i in range(long(s[0]),long(s[1])+1):
            if pal(i) and sqrt_of_pal(i):
                tot = tot + 1
        output.write("Case #%d: %s\n" % (tc+1, tot) )

