t=int(input())
for i in range(1,t+1):
    string,k = list(input().split())
    string=list(string)
    k=int(k)
    flag=0
    for j in string:
        if(j=='-'):
            flag=1
            break
    if(flag==0):
        print("Case #{}: 0".format(i))
    else:
        count=0
        h=0
        while(h<len(string)-k+1):
            if(string[h]=='-'):
                count+=1
                for s in range(k):
                    if(string[h+s]=='-'):
                        string[h+s]='+'
                    else:
                        string[h+s]='-'
            h+=1
        for j in string:
            if(j=='-'):
                print("Case #{}: IMPOSSIBLE".format(i))
                flag=0
                break
        if(flag==1):
            print("Case #{}: {}".format(i, count))
