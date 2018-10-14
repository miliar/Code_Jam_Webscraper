def friends(a):
    n=0
    s=0
    for j in range(len(a)):
        if(s<j):
            n=n+j-s
            s=s+j-s
        s=s+int(a[j])
    return str(n)

def ovation (file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        (m,a)=f.readline()[:-1].split(' ')
        m=int(m)
        c=friends(a)
        g.write("Case #"+str(x+1)+": "+str(c)+"\n")
    f.close()
    g.close()
