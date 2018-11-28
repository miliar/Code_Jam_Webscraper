def check(count,ans,inp,j):
    if count >= j:
        count+=inp
        return (count,ans)
    else:
        return check(count+1,ans+1,inp,j)
howmany = int(raw_input())
for i in range(1,howmany+1):
    inp = raw_input().split(" ")
    count = 0
    ans = 0
    for j in range(0,int(inp[0])+1):
        temp = check(count,ans,int(inp[1][j]),j)
        count = temp[0]
        ans = temp[1]
    print "Case #"+str(i)+": "+str(ans)
