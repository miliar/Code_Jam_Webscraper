def perno(n):
    lp=[n[0]]
    for x in range(len(n)-1):
        if (n[x]!=n[x+1]):
            lp.append(n[x+1])
    ps=''.join(lp)

    if (len(ps)==1):
        return n
    
    for y in range(len(ps)-1):
        if (ps[y]>ps[y+1]):
            b=0
            break
        b=1

    if (b==1):
        return n

    a=n.find(ps[y])

    f=n[:a]+str(int(n[a])-1)+'9'*(len(n)-a-1)

    if (f[0]=='0'):
        f=f[1:]
    return f

def tidy(file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        m = f.readline()[:-1]
        c=perno(m)
        g.write("Case #"+str(x+1)+": "+str(c)+"\n")
    f.close()
    g.close()
