f=open('small.txt', 'r')
g=open('outputsmall.txt','w')
data=[]

for line in f:
    data.append(line.split(" "))

for i in range(int(data[0][0])):
    sum=int(data[i+1][1][0])
    n=0
    for j in range(int(data[i+1][0])):
       if sum + n < j+1:
           n += j+1-sum-n
           sum+=int(data[i+1][1][j+1])
       else:
           sum+=int(data[i+1][1][j+1])
    print('Case #'+str(i+1)+': '+str(n))
    g.write('Case #'+str(i+1)+': '+str(n)+'\n')

g.close()
    
    

