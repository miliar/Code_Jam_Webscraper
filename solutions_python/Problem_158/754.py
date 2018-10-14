f=open('small.txt', 'r')
g=open('outputsmall.txt','w')

data=[]
inside=[]
x=int(f.readline())
for a in range(x):
    data.append(f.readline().split(" "))
    for char in range(3):
        data[a][char]=int(data[a][char])

print(data)

for a in range(x):
    if data[a][0]==1:
        n="GABRIEL"
    elif (data[a][1]*data[a][2])%data[a][0]!=0:
        n="RICHARD"
    elif data[a][0]==2:
        n="GABRIEL"
    elif data[a][0]==3:
        if (data[a][1]*data[a][2])==3:
            n="RICHARD"
        else:
            n="GABRIEL"
    elif data[a][0]==4:
        if (data[a][1]*data[a][2])==4:
            n="RICHARD"
        elif (data[a][1]*data[a][2])==8:
            n="RICHARD"
        else:
            n="GABRIEL"
    print('Case #'+str(a+1)+': '+str(n))
    g.write('Case #'+str(a+1)+': '+str(n)+'\n')

g.close()


