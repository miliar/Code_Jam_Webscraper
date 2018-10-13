data=open('in.txt','r')
a=[]
for line in data:
    a.append(line)
n=int(a[0])
for i in range(n):
    m=int(a[i+1][0])
    stand=int(a[i+1][2])
    friend=0
    for j in range(3,2+m+1):
        people=int(a[i+1][j])
        if(stand>=j-2):
            stand=stand+people
        else:
            f=j-2-stand
            friend=friend+f
            stand=stand+people+f
    print('Case #',i+1,': ',friend,sep='')
    
