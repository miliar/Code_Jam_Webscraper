__author__ = 'peter'
import sys
res=[]
with open("B-large.in","r") as inF:
    t= int(inF.readline())
    for it in xrange(t):
        n= int(inF.readline())
        s= map(int, inF.readline().split())
        currRes=0
        for i in xrange(n):
            minZ= sys.maxint
            minInd=-1
            for j in xrange(len(s)):
                if minZ>s[j]:
                    minInd=j
                    minZ=s[j]
            sp= (len(s)-1)-minInd
            if sp>minInd:
                sp=minInd
            currRes+=sp
            s.pop(minInd)
        res.append(currRes)

with open("B-large.out","w") as outF:
    for it in xrange(t):
        outF.write("Case #%d: %d\n"%(it+1,res[it]))