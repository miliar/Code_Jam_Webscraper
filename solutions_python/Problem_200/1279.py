f=open("B-large.in",'r')
pp=f.readlines()
for k in range(int((pp[0].split("\n"))[0])):
    g=k+1
    s=(pp[g].split("\n"))[0]
    a=list(str(s))
    p=a+[]
    m='9'
    for i in xrange(1,len(a)+1):
        r=0
        if (i!=len(a) and p[-i]=='0'):
            r=1
            p[-i]='9'
            if ((i+1)<=len(a)):
                if (p[-(i+1)]!='0'):
                    p[-(i+1)]=str(int(p[-(i+1)])-1)
        

        if (p[-i]>m and i>=2):
            if (r==0):
                p[-i]=str(int(p[-i])-1)
            p[-(i-1):]='9'*len(p[-(i-1):])
            r=1

        m=p[-i]
    v=int(''.join(p))
    print "Case #"+str(g)+": "+str(v)

    
        
