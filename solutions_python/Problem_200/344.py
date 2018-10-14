t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":",
    inp = map(int,list(raw_input()))
    ans = []
    change = False
    while(len(inp)!=0):
        curr = inp[0]
        if(change == True):
            curr = 9
        inp.pop(0)
        ans += [curr]
        while(len(ans) > 1 and (ans[-1]<ans[-2])):
            inp = [ans[-1]]+inp
            ans.pop(-1)
            ans[-1]-=1
            change = True
    while(ans[0]==0):
        ans.pop(0)
    ans = map(str,ans)
    print "".join(ans)
            
