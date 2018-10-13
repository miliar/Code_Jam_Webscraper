f=open('A-small-attempt1.in','r')
f1=open('A-small-attempt1.out','a')
n=f.readline()
print n
x=0
a=f.readlines()
for num in range(0,int(n)):
    i=0
    z=[]
    r={}
    s={}
    for num1 in range(0,2):
        p=a[x]
        #print p
        y=int(p)+x
        z.append(a[y])
        x+=5
    #print z
    r=z[0].split( )
    #print r
    s=z[1].split( )
    q=list(set(r).intersection(s))
    #print q
    b=0
    for num2 in range(len(q)):
        if q[num2].isdigit():
            b+=1
    if b==1:
        for num2 in range(len(q)):
            if q[num2].isdigit():
                data="Case #%d: %d\n"%(num+1,int(q[num2]))
                #print >> f1,"Case#%d: %d"%(num+1,int(q[num2]))
                f1.write(data)
    elif b==0:
        data="Case #%d: Volunteer cheated!\n"%(num+1)
        f1.write(data)
        #print >> f1,"Case#%d: volunteer cheated!"%(num+1)
    else:
        data="Case #%d: Bad magician!\n"%(num+1)
        f1.write(data)
        #print >> f1,"Case#%d: Bad magician!"%(num+1)
