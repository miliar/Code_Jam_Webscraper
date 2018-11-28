from string import split
f1=open('B-large.in','r')
f2=open('out.txt','w')
t=int(f1.readline())
for i in range (t):
    k=0
    s=f1.readline()
    data=list(map(int,s.split(' ')))
    u=data[1]+0
    for j in range(data[0]):
        if data[j+3]==0 or data[j+3]==1:
            if data[j+3]>=data[2]:
                k+=1
        elif data[1]==0:
            if data[j+3] % 3==0 and data[j+3]//3>=data[2]:
                k+=1
            elif data[j+3]%3!=0 and data[j+3]//3+1>=data[2]:
                k+=1
        else:
            if data[j+3]%3==1 and data[j+3]//3+1>=data[2]:
                k+=1
            elif data[j+3]%3==0 and data[j+3]//3+1==data[2] and u!=0:
                u-=1
                k+=1
            elif data[j+3]%3==0 and data[j+3]//3>=data[2]:
                k+=1
            elif data[j+3]%3==2 and data[j+3]//3+2==data[2] and u!=0:
                u-=1
                k+=1
            elif data[j+3]%3==2 and data[j+3]//3+1>=data[2]:
                k+=1
    f2.write ("Case #"+str(i+1)+": "+str(k)+"\n")
f1.close()
f2.close()
