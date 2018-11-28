def _gcd(m,n):
    if n==0:
        return m
    return _gcd(n,m%n)

def gcd(l,i,j):
    if i==j:
        return l[i]
    k=(i+j)/2
    return _gcd(gcd(l,i,k),gcd(l,k+1,j))

def solvecase(index):
    line=[int(e) for e in raw_input().split()]
    line.pop(0)
    dline=[]
    for i in range(len(line)):
        for j in range(1,len(line)):
            if line[i]-line[j]>0:
                dline.append(line[i]-line[j])
                if line[j]-line[i]>0:
                dline.append(line[j]-line[i])
    d=gcd(dline,0,len(dline)-1)
    x=max(line)
    y=(x/d)*d
    if x%d!=0:
        y+=d
    print "Case #%d: %d"%(index,y-x)
    
if __name__ == '__main__':
    t=int(raw_input())
    for i in range(t):
        solvecase(i+1)
