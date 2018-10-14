t=int(input())
q=[]
for i in range(t):
    n,k=map(int, input().split())
    q.append([n,k])

for i in range(t):
    n,k=q[i][0],q[i][1]
    a=[n//2 - (n%2 == 0), n//2]
    if k==1:
        print("Case #"+str(i+1)+": "+str(max(a[0],a[1]))+" "+str(min(a[0],a[1])))
        continue
    if k==n:
        print("Case #"+str(i+1)+": 0 0")
        continue
    cnt=0
    while cnt<k-1:
        m=max(a)
        if m!=1 or m!=0:
            a.append(m//2 - (m%2 == 0))
            a.append(m//2)
            l=m//2 - (m%2 == 0)
            r=m//2
            a.remove(m)
        else:
            if m==1:
                a.append(0)
                a.append(0)
                a.remove(1)
                l=0
                r=0
        cnt+=1
    print("Case #"+str(i+1)+": "+str(max(l,r))+" "+str(min(l,r)))
