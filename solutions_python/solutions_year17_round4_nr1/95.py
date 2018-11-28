T=int(input())
for t in range(T):
    line=input().split()
    n=int(line[0])
    p=int(line[1])
    line=input().split()
    r=[0 for i in range (p)]
    for i in range (n):
        c=int(line[i])
        r[c%p]+=1
    if (p==2):
        s=r[0]+(r[1]+1)//2
    if (p==3):
        s=r[0]+min(r[1],r[2]) + (abs(r[1]-r[2])+2)//3
    if (p==4):
        s=r[0] + r[2]//2 + min(r[1],r[3])
        s+= (2*(r[2]%2) + abs(r[1]-r[3]) +3)//4
    print ("Case #" + str(t+1) + ": " + str(s))
