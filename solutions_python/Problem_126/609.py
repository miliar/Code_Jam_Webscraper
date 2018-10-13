def substr(s,n):
    l = len(s)
    result  = []
    for x in xrange(n,l+1):
        result += [s[i:(i + x)] for i in xrange(l - x + 1)]
    return result
import re
cases   = int(raw_input())
for z in xrange(cases):
    ip  = raw_input().split()
    s   = str(ip[0])
    n   = int(ip[1])
    su  = substr(s,n)
    ans = 0
    for y in xrange(len(su)):
        if re.search(r"[^aeiou]{"+str(n)+"}",su[y]):
            ans+=1
    print "Case #"+str(z+1)+": "+str(ans)