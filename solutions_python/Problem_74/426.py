x='inp.txt'

def z():
    global st
    s=0
    x0=1
    xb=1
    orde='o'
    for L in range(len(st)):
        k=L;
        if st[k][0]=='o':
            g0=st[k][1]
            p=2-2;
            for l in range(k+1,len(st),1):
                if st[l][0]=='b':
                    gb=st[l][1]
                    if gb-xb>=0:db=1
                    else:   db=-1
                    p=1
                    break 
            l=g0-x0
            x0=g0
            #print('o',g0-l,x0,p)
            if l>=0:
                 da=1
            else:
                 da=-1
            if p==1:
                 l=(l*da+1)
                 xb+=l*db
                 if xb>=gb and db==1 or xb<=gb and db==-1:
                     xb=gb
                
            else:
                 l=l*da+1    
            s+=l
            #print('s ',s)
        elif st[k][0]=='b':
            gb=st[k][1]
            p=2-2
            for l in range(k+1,len(st),1):
                if st[l][0]=='o':
                    g0=st[l][1]
                    p=1
                    if g0-x0>=0:da=1
                    else:   da=-1
                    break
            l=gb-xb
            xb=gb
            #print('o',gb-l,xb,p)
            if l>=0:
                db=1
            else:
                db=-1
            if p==1:
                l=(l*db+1)
                x0+=l*da
                if x0>=g0 and da==1 or x0<=g0 and da==-1:
                    x0=g0
            else:
                l=l*db+1
            s+=l
            #print('s ',s)
    return int(s)

with open(x,'r') as Z:
    i=Z.readlines()

t=int(i[0])
i=i[1:]
zds=[]
for s in i:
    a=s.split()
    n=int(a[0])
    st=[]
    for d in range(int(n)):
        st.append([a[2*d+1].lower(),int(a[2*d+2])])
    print(st)
    zds.append(z())

z_=open('out.txt','w')
for d in range(len(zds)):z_.write('Case #'+str(d+1)+': '+str(zds[d])+'\n')
z_.close()

print('end')

  
