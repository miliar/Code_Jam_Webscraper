def move(n,i):
    j=len(str(n))-i
    m=int(str(n)[-i:])*10**j + int(str(n)[:j])
    return m
    
#f=open('test.in','r')
f=open('C-small-attempt2.in','r')
r=open('result.txt','w')



T=int(f.readline())
t=0
for i in range(T):
    line = f.readline().strip()
    t+=1
    count=0
    dic={}
    A=int(line.split(' ')[0])
    B=int(line.split(' ')[1])
    if B<=9:
       r.write('Case #'+str(t)+': 0\n') 
    else:
        for N in range(A, B):
            for l in range(1,len(str(A))):
                M=move(N,l)
                if M>N and M<=B:
                    if str(N)+str(M) in dic:
                        continue
                    else:
                        count+=1
                        dic[str(N)+str(M)]=1
        r.write('Case #'+str(t)+': '+str(count)+'\n')  

f.close()
r.close()
