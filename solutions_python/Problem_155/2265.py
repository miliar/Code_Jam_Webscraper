a=""
c=0
s=0
count=0
b=[]
T=int(input())
for i in range(T):
    a=input()
    b.append(a.split(" "))
for j in range(T):
    c=0
    count=0
    s=0
    while c<=int(b[j][0]):
        if s>=c:
            s=s+int(b[j][1][c])
        else:
            count=count+(c-s)
            s=s+(c-s)+int(b[j][1][c])
        c=c+1    
    print("Case #%d: %d"%(j+1,count))