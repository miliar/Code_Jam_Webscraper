T = int(raw_input().strip())

for test in range(1,T+1):
    smax,people = raw_input().strip().split()
    smax = int(smax)
    p = []
    for i in people:
        p.append(int(i))
    stand = p[0]
    ans = 0
    for i in range(1,smax+1):
        if(p[i] != 0):
            if(stand >= i):
                stand += p[i]
            else:
                ans += i-stand
                stand = i+p[i]
        #print i,ans,stand
    print "Case #" + str(test) + ": " + str(ans)
