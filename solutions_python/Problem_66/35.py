import math
max=100000*pow(2,11)

f=open('B-large(2).in','r')
g=open('B-large.out','w')
getline=f.readline()
#eleline=getline.split()

tt=int(getline)


for case in range(tt):
    getline=f.readline()
    p=int(getline)
    n=pow(2,p)

    getline=f.readline()    
    eleline=getline.split()

    miss=[0 for i in range(n)]
#    print max,p,n,eleline
    
    for i in range(n):
        miss[i]=int(eleline[i])
        miss[i]=p-miss[i]
        

    for i in range(n/2):
        miss[i]=miss[2*i]
        if miss[2*i+1]>miss[i]:
            miss[i]=miss[2*i+1]
    n=n/2
    #print miss 
    price=[[0 for i in range(n)] for j in range(p)]
    dp=[[0 for i in range(p)] for j in range(n)]
    np=[[0 for i in range(p)] for j in range(n)]
    for i in range(p):
        getline=f.readline()    
        eleline=getline.split()
        for j in range(pow(2,p-i-1)):
            price[i][j]=int(eleline[j])

    for i in range(n):
        for j in range(p):
            if j>=miss[i]:
                dp[i][j]=0
            else:
                if j>=miss[i]-1:
                    dp[i][j]=price[0][i]
                else:
                    dp[i][j]=max
   # print dp[2][1],dp[2][2],dp[1][1],dp[0][1],dp[3][2]
    #print price[p-1][0]

    for k in range(1,p):
        for i in range(pow(2,p-k-1)):
            s1=2*i;s2=2*i+1;
            for j in range(p-k):
                np[i][j]=min(dp[s1][j]+dp[s2][j],dp[s1][j+1]+dp[s2][j+1]+price[k][i])
        #print np[0][0],np[0][1],np[1][1]
        for i in range(pow(2,p-k-1)):
            for j in range(p-k):
                dp[i][j]=np[i][j]        
    
    ans=dp[0][0]
    print 'Case #'+str(case+1)+': '+str(ans)+'\n'
    g.write('Case #'+str(case+1)+': '+str(ans)+'\n')


f.close()
g.close()

            


