import sys
kapping=" abcdefghijklmnopqrstuvwxyz"
mapping=" ynficwlbkuomxsevzpdrjgthaq"
f=sys.stdin
n=int(f.readline())
for i in range(0,n):
    tmp=f.readline()[:-1]
    res=""
    for j in tmp:
        res+=kapping[mapping.index(j)]
    print "Case #%d: %s"%(i+1,res)
