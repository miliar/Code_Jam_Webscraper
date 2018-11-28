# cook your dish here
t=int(input())
k=1
while(t>0):
    n=int(input())
    while(n>0):
        count=0
        str1=str(n)
        for i in range(1,len(str1)):
            if(int(str1[i])-int(str1[i-1])<0):
                count=1
                break
        if(count==0):
            break
        n-=1
    print("Case #"+str(k)+": "+str(n))
    k+=1
    t-=1