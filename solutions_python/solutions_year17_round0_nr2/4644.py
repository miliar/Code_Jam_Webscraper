
import sys

n = int(raw_input())

def is_tidy(numstr):
    prev = numstr[0]
    ret = True
    for i in xrange(1,len(numstr)):
        if int(numstr[i]) < int(prev):
            ret = False
            break
        prev = numstr[i]
    return ret

for i in xrange(1,n+1):
    t = int(raw_input())
    ans = 0
    for j in xrange(t,0,-1):
        if is_tidy(str(j)):
            ans = j
            break
    print "Case #"+str(i)+": "+str(ans)
