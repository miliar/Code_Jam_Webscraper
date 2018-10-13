f=open('input','r')
t=int(f.readline())
def compress(st):
    prev=''
    alp=[]
    ct=[]
    temp=1
    for e in st:
        if e==prev:
            temp+=1
        else:
            alp.append(prev)
            ct.append(temp)
            temp=1
            prev=e
    alp.append(e)
    ct.append(temp)
    return alp[1:],ct[1:]

for case in xrange(1,t+1):
    flag=0
    n=int(f.readline())
    st=[]
    alp=[]
    ct=[]
    for e in xrange(n):
        st.append(f.readline().strip())
        a,b=compress(st[-1])
        alp.append(a)
        ct.append(b)
    for i in xrange(len(st)-1):
        if alp[i]!=alp[i+1]:
            print 'Case #%d: Fegla Won'%case
            flag=1
            break
    if flag==1:
        continue
    trg=[]
    for i in xrange(len(ct[0])):
        mi=[0,9999999]
        for md in xrange(0,101):
            su=0
            for j in xrange(len(ct)):
                su+=abs(md-ct[j][i])
            if su<mi[1]:
                mi[0]=md
                mi[1]=su
        trg.append(mi[1])
    print 'Case #%d: %d'%(case,sum(trg))
            
    
        
