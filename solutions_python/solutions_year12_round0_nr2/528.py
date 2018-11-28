def solve(s,p,a):
    if p==0: return len(a)
    res = 0
    if p==1:
        for x in a:
            if x>0: res+=1
        return res
    p = p + p-2 + p-2
    for x in a:
        if x>p+1: res+=1
        elif s>0:
            if x>=p: 
                res+=1
                s-=1
    return res

fi = open("input.txt")
nTest = int(fi.readline())

for test in range(nTest):
    a = map(int,fi.readline().split())
    n,s,p = a[:3]
    a = a[3:]
    assert len(a)==n
    print "Case #"+str(test+1)+":",solve(s,p,a)