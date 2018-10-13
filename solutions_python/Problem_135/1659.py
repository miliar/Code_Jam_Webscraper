T=int(input())

for t in range(0,T):
    R1=int(input())
    for i in range(1,5):
        L=input()
        if i==R1:
            r1=L.split()
    R2=int(input())
    for i in range(1,5):
        L=input()
        if i==R2:
            r2=L.split()
    c = 0
    for i in range(0,4):
        for j in range(0,4):
            if r1[i] == r2[j]:
                c = c + 1
                ans = int(r1[i])
    if c==0:
        print("Case #%d: Volunteer cheated!"%(t+1))
    elif c==1:
        print("Case #%d: %d"%(t+1, ans))
    else:
        print("Case #%d: Bad magician!"%(t+1))
   
