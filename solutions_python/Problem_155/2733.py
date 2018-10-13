def solve():
    n,shyness = raw_input().split()
    ans=0
    cnt=0
    for i in range(len(shyness)):
        if cnt < i:
            ans+=1
            cnt=i+int(shyness[i])
        else:
            cnt+=int(shyness[i])
    return ans


for i in range(int(raw_input().strip())):
    ans = solve()
    print "Case #%d: %s" % (i+1, ans)
