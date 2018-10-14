f=open('c:/A-large.in','r')
answer=open('c:/answer3.txt','w+')
T=int(f.readline())
for i in range(T):
    a=f.readline()
    ls=a.split()
    max=int(ls[0])
    st=ls[1]
    sum=0
    num=0
    for j in range(max+1):
        if int(st[j])==0:
            continue
        elif sum<j:
            num=j-sum+num
            sum=j+int(st[j])
        else:
            sum=sum+int(st[j])
    answer.write('Case #%d: %d\n'%(i+1,num))
f.close()
answer.close()
