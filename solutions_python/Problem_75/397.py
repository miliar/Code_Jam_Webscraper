num = int(raw_input())
for n in range(1,num+1):
    inp = raw_input().split()
    rp = {}
    rm = []
    seq = inp[len(inp)-1]
    for i in range(1,int(inp[0])+1):
        rp[inp[i][0]+inp[i][1]] = inp[i][2]
        rp[inp[i][1]+inp[i][0]] = inp[i][2]
    num_rm=inp[int(inp[0])+1]
    k = int(num_rm)
    for i in range(1,k+1):
        rm.append(inp[int(inp[0])+1+i])
    ans = []
    for i in seq:
        ans.append(i)
        if(len(ans) > 1):
            while(ans[len(ans)-1] + ans[len(ans)-2] in rp.keys() ):
                a = rp[ans[len(ans)-1] + ans[len(ans)-2]]
                ans.pop()
                ans.pop()
                ans.append(a)
            for j in rm:
                if(j[0] in ans and j[1] in ans):
                    ans = []
    print 'Case #' + str(n) + ': [' + str.join(', ',ans) + ']'
