f = open("A-small-attempt4.in","r")

t=f.readline()
ans = []
for i in range(0,int(t)):
    x=f.readline()
    x1=f.readline().split()
    v1=[int(y) for y in x1]
    x2=f.readline().split()
    v2=[int(y) for y in x2]
    x3=f.readline().split()
    v3=[int(y) for y in x3]
    x4=f.readline().split()
    v4=[int(y) for y in x4]
    d=f.readline()
    y1=f.readline().split()
    j1=[int(y) for y in y1]
    y2=f.readline().split()
    j2=[int(y) for y in y2]
    y3=f.readline().split()
    j3=[int(y) for y in y3]
    y4=f.readline().split()
    j4=[int(y) for y in y4]
    z=[v1,v2,v3,v4]
    a=[j1,j2,j3,j4]
    b=z[int(x)-1]
    c=a[int(d)-1]
    z1=[b,c]
    z11=z1[0]
    z12=z1[1]
    sum = []
    for i in range(0,4):
        for j in range(0,4):
            if z11[i]==z12[j]:
                sum.append(z11[i])
            else:
                sum = sum
                
    if len(sum)==0:
        ans.append(str("Volunteer cheated!"))
    elif len(sum)==1:
        ans.append(sum[0])
    else:
        ans.append(str("Bad magician!"))
        
for i in range(0,int(t)):
    print("Case #"+str(i+1)+": "+str(ans[i]))
   
   
