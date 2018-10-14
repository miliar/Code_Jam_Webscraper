#Meet Shah - DAIICT
#GCJ Qualification A
t = int(input())
for xx in range(t):
    foo = input().split()
    arr = list(foo[0])
    n = int(foo[1])
    ans = 0
    #print(n,arr)
    if(n==1):
        ans = arr.count('-')
    else:
        for i in range(len(arr)-n+1):
            if(arr[i]=='+'):
                #print("1",arr)
                continue
            elif(arr[i]==arr[i+1] and arr[i]=='-'):
                ans+=1
                for j in range(i,n+i):
                    if(arr[j]=='+'):
                        arr[j]='-'
                    else:
                        arr[j]='+'
                #print("2",arr)
            elif(arr[i]==arr[i+1] and arr[i]=='+'):
                i+=1
                #print("3",arr)
            
            else:
                ans+=(1)
                for j in range(i,i+n):
                        if(arr[j]=='-'):
                            arr[j]='+'
                        else:
                            arr[j]='-'
                #print("4",arr)
        if(arr==(['+']*len(arr))):
            print("Case #",xx+1,": ",ans,sep='')
        else:
            print("Case #",xx+1,": IMPOSSIBLE",sep='')
                    