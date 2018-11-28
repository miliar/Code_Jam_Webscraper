t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":",
    ans = 0
    inp = raw_input().split()
    x = list(inp[0])
    k = int(inp[1])
    l = len(x)
    for i in xrange(0,(l-k)+1):
        if(x[i]=='-'):
            ans += 1
            for j in xrange(k):
                if(x[i+j]=='-'):
                    x[i+j]='+'
                else:
                    x[i+j]='-'
    if('-' in x):
        ans = "IMPOSSIBLE"
    print ans
