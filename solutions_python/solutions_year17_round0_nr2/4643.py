t =int(input())
for ti in range(t):
    n = int(input().strip())
    ans=0
    for i in range(n,0,-1):
        x=list(str(i))
        flag=1
        #print(x)
        for k in range(1,len(x)-1,1):
            if(x[k]=='0' and x[k+1]!='0'):
                x[0]=chr(ord(x[0])-1)
                for l in range(1,len(x)):
                    x[l]='9'
                flag=2
                break
        for j in range(len(x)-1):
            if(x[j]>x[j+1]):
                flag=0
                break
        if(flag==1):
            ans=i
            break
        if(flag==2):
            ans=int(''.join(x))
            break
    print("Case #",ti+1,": ",ans,sep='')
