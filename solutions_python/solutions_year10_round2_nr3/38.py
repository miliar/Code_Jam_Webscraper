import math
num=100003

f=open('c-small-practice.in','r')
g=open('c-large-1.out','w')
getline=f.readline()

t=int(getline)
print t


com=[[0 for i in range(501)] for j in range(501)]
com[0][0]=1
for i in range(1,501):
    com[i][0]=1;com[i][i]=1;
    for j in range(1,i):
        com[i][j]=(com[i-1][j]+com[i-1][j-1])% num;

a=[[0 for i in range(501)] for j in range(501)]

for j in range(2,500+1):
    a[j][1]=1

for i in range(2,500+1):
    for j in range(i+1,500+1):
        for k in range(1,i):
            a[j][i]=(a[j][i]+a[i][k]*com[j-i-1][i-k-1])%num
for case in range(t):
    getline=f.readline()
    n=int(getline)
    print n


        
    ans=0;

    for i in range(1,n+1):
        ans=(ans+a[n][i])%num
    g.write('Case #'+str(case+1)+': '+str(ans)+'\n')
    #print 'Case #'+str(case+1)+': '+str(ans)+'\n'

f.close()
g.close()

            


