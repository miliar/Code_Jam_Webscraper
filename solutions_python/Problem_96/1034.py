#f=open('test.in','r')
f=open('B-large.in','r')
r=open('result.txt','w')

T=int(f.readline())

for i in range(T):
    ti=[]
    count=0
    t+=1
    line = f.readline().strip()
    N=int(line.split(' ')[0])
    S=int(line.split(' ')[1])
    p=int(line.split(' ')[2])
    for j in line.split(' ')[3:]:
        ti.append(int(j))
    for t in ti:
        a=t/3
        b=t%3

        if a>=p:
            count+=1
        elif b==1 and a+b>=p:
            count+=1
        elif b==2 and a+1>=p:
            count+=1
        elif b==2 and a+2>=p and S>0:
            count+=1
            S-=1
        elif b==0 and a!=0 and a+1>=p and S>0:
            count+=1
            S-=1
    r.write('Case #'+str(i+1)+': '+str(count)+'\n')   
    
    

f.close()
r.close()
