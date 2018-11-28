file=open("B-large.in",'r')
t=int(file.readline())
out=open("out2.txt",'w')
for i in range(1,t+1):
    num=int(file.readline())
    j=1
    q=[]
    for d in str(num):
        q.append(int(d))
    j=0 
    l=len(q)-1
    while True:
        b=q.copy()
        b.sort()
        if l>0:    
            if q!=b and q[l]<q[l-1]:
                q[l]=9
                q[l-1]-=1
                l-=1
            elif q!=b and q[l]>=q[l-1]:
                q[l]=9
                l-=1 
            else:
                l-=1               
        else:
            break   
    s=''
    for j in q:
        s+=str(j)
    s=int(s)    
    out.write('Case #%d: %d\n'%(i,s))       
file.close()
out.close()                 
