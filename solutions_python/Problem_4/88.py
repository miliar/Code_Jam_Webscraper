f=open("A-large.in")
w=open("a-out.txt",'w')
s=f.read().split('\n')
n=int(s.pop(0))
j=1
while n!=0:
    n-=1
    s.pop(0)
    v1=s.pop(0).split(' ')
    v2=s.pop(0).split(' ')
    for i in range(len(v1)):
        v1[i]=int(v1[i])
        v2[i]=int(v2[i])
    
    v1.sort()
    v2.sort()
    v2.reverse()
    s1=0
    for i in range(len(v1)):
        s1=s1+v1[i]*v2[i]
    w.write("Case #"+str(j)+": " + str(s1)+'\n')
    j+=1
w.close()
f.close()
