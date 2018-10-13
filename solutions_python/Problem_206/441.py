for t in xrange(input()):
    d,n = map(int,raw_input().strip().split())
    horses = []
    for i in range(n):
        horses.append(map(float,raw_input().strip().split()))
    horses = sorted(horses,key=lambda x:x[0],reverse = True)
    ans = [None]*n
    ans[0] = (d-horses[0][0])/horses[0][1]
    for i in range(1,n):
        time = (d-horses[i][0])/horses[i][1]
        if time < ans[i-1]:
            time = ans[i-1]
        ans[i] = time
        #print ans
    print "Case #{}: {}".format(t+1,d/ans[-1])