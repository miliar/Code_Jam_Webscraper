fob=open('B-large.in','r')

T=int(fob.readline())##test cases
n=2
la=[]##answer list
for i in range(T):
    c,f,x=fob.readline().split()
    c,f,x=float(c),float(f),float(x)
    flag=0
    t1=x/n
    t=0
    while(flag==0):
        t=t+c/n
        n=n+f
        t2=x/n+t
        if(t1>=t2):
            t1=t2
        else:
            n=2
            break
    la.append(t1)
for i in range(T):
    print 'Case #'+str((i+1))+':',la[i]
fob.close()
