import psyco
psyco.full()

def getbase(n, base, digit=None):
    ret=[]
    while (True):
        if (n<base):
            ret.append(n)
            break
        r=n%base
        n=n/base
        ret.append(r)
    ret.reverse()
    if digit!=None:
        ret=[[]]*(digit-len(ret))+ret
    return ret

def inputIntList():
    return [int(e) for e in raw_input().split()]

def geti(m,k,s):
    return min([m.index(i,s) for i in xrange(k+1) if i in m[s:]])

def solve(mat,N):
    m=[]
    for s in mat:
        if "1" in s:
            m.append(s.rindex("1"))
        else:
            m.append(0)
    #print m
    chgcount=0
    for i in range(N):
        fi=geti(m,i,i)
        chgcount+=fi-i
        m=m[:i]+[m[fi]]+m[i:fi]+m[fi+1:]
    return chgcount

caseNum=input()
for caseId in xrange(1, caseNum+1):
    N=input()
    mat=[]
    for n in xrange(N):
        mat.append(raw_input())
    print "Case #%d: %d" % (caseId, solve(mat,N))
