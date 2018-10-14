ans=[]
for i in range(int(input())):
    d,n=map(int, input().split())
    a=[]
    for j in range(n):
        k,s=map(int, input().split())
        a.append(float(d-k)/s)
    ans.append("Case #"+str(i+1)+": "+str(d/max(a)))

for i in ans:
    print(i)
