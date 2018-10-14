for i in range(int(input())):
    inp=list(map(str, input().split()))
    pans=list(inp[0])
    k=int(inp[1])
    ans=0
    while True:
        if '-' not in pans:
            print("Case #{}: {}".format(i+1, ans))
            break
        else:
            a=pans.index('-')
            if(a+k>len(pans)):
                print("Case #{}: {}".format(i+1, "IMPOSSIBLE"))
                break
            for j in range(k):
                if pans[a+j]=='-' :
                    pans[a+j]='+'
                else:
                    pans[a+j]='-'
            ans+=1
    
