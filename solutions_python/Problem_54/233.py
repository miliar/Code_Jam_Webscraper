def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a
T=int(raw_input())
for i in range(T):
    inp=raw_input().split()
    N=int(inp[0])
    l=[int(e) for e in inp[1:]]
    l.sort()
    diff=[]
    for j in range(N-1):
        diff.append(int(l[j+1])-int(l[j]))
    g=reduce(gcd,diff)
    last=int(l[0])
    #y+last=a*gcd
    #y=a*gcd-last
    if(last%g==0):
        a=last/g
    else:
        a=last//g +1  
    print 'Case #%d: %d'%(i+1,a*g-last)
    
