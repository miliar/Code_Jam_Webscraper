import sys
import re

input=sys.stdin

CS={}
def strsort(s):
    if s not in CS:
        ss=[int(x) for x in s]
        ss.sort()
        CS[s]=''.join(map(str,ss))
    return CS[s]

def eq(a,b):
    a=str(a)
    b=str(b)
    re.sub('0','',a)
    re.sub('0','',b)
    return strsort(a)==strsort(b)

def change(s):
    s=str(s)
    if len(s)==1:
        return s+'0'
    ints=[int(x) for x in s]
    #print s
    try:
        b=False
        for i in xrange(len(s)-1,1,-1):
            if ints[i-1]<ints[i]:
                b=True
                break
        if b:
            res=''.join(s[:i-1])
            ss=ints[i-1:]
            ssf=[x for x in ss if x>ss[0]]
        else:
            if ints[0]<ints[1]:
                res=''
                ss=[x for x in ints]
                ssf=[x for x in ss if x>ints[0]]
            else:
                raise
        ssf.sort()
        res=res+str(ssf[0])
        ss.remove(ssf[0])
        ss.sort()
        res=res+''.join(map(str,ss))
    except:
        ss=ints
        ssf=[x for x in ss if x>0]
        res=''
        ssf.sort()
        res=res+str(ssf[0])
        ss.remove(ssf[0])
        ss.append(0)
        ss.sort()
        res=res+''.join(map(str,ss))
    return res

T=int(input.readline())
for i in xrange(1,T+1):
    N=int(input.readline())
    n=change(N)
    #k=N+1
    #while not eq(N,k) :
    #    k+=1
    #if n!=k:
    #    print n,k
    print "Case #%s: %s" %(i,n)
