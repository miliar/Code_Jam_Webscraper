f=open('small1.txt', 'r')
g=open('outputsmall.txt','w')

data=[]
inside=[]
x=int(f.readline())
for a in range(x):
    inside.append(int(f.readline()))
    inside.append(f.readline().split(" "))
    for char in range(inside[0]):
        inside[1][char]=int(inside[1][char])
    data.append(inside)
    inside=[]

def method1(l):
    j=0
    for i in range(l[0]-1):
        if l[1][i]-l[1][i+1]>0:
           j+=l[1][i]-l[1][i+1]
        else:
            j+=0
    return j

def method2(l):
    l1=[]
    for i in range(l[0]-1):
        if l[1][i]-l[1][i+1]>0:
            l1.append(l[1][i]-l[1][i+1])
        else:
            l1.append(0)
    j=max(l1)
    k=0
    for i in range(l[0]-1):
        if l[1][i]<j:
            k+=l[1][i]
        else:
            k+=j
    return k

for a in range(x):
    n=method1(data[a])
    m=method2(data[a])
    print('Case #'+str(a+1)+': '+str(n),str(m))
    g.write('Case #'+str(a+1)+': '+str(n)+' '+str(m)+'\n')

g.close()


