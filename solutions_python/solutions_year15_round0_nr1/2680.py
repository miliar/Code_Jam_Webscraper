inf=open('input.txt','r')
of=open('output.txt','w')

n=int(inf.readline())
for k in range(n):
    s=inf.readline()
    a,b=s.split(' ')
    a=int(a)
    s=[]
    for i in range(a+1):
        s.append(int(b[i]))
    o=0
    p=0
    for i in range(a+1):
        if(p<i):
            o+=(i-p)
            p+=(i-p)
        p+=s[i]
    of.write('Case #'+str(k+1)+': '+str(o)+'\n')
inf.close()
of.close()
