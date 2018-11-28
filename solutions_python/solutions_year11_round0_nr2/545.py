test = int(raw_input())
for n in range(1,test+1):
    x = raw_input().split()
    comb = {}
    oppse = []
    seq = x[len(x)-1]
    for i in range(1,int(x[0])+1):
        comb[x[i][0]+x[i][1]] = x[i][2]
        comb[x[i][1]+x[i][0]] = x[i][2]
    k = int(x[int(x[0])+1])
    for i in range(1,k+1):
        oppse.append(x[int(x[0])+1+i])
    ans = []
    for i in seq:
        ans.append(i)
        if(len(ans) > 1):
            while(ans[len(ans)-1] + ans[len(ans)-2] in comb.keys() ):
                a = comb[ans[len(ans)-1] + ans[len(ans)-2]]
                ans.pop()
                ans.pop()
                ans.append(a)
            for j in oppse:
                if(j[0] in ans and j[1] in ans):
                    ans = []
    ss = ''
    if(ans != []):
        for k in range(len(ans)-1):
            ss += ans[k] + ',' + ' '
        ss += ans[len(ans)-1]
    print 'Case #' + str(n) + ': [' + ss + ']'
