T = int(raw_input())
for _case_ in xrange(T):
    Smax, S = raw_input().split()
    ans = 0
    count = 0
    i = 0
    for i in xrange(int(Smax)+1):
        num = int(S[i])
        if count < i:
            ans += i - count
            count = i
        count += num
    print "Case #"+str(_case_+1)+": "+str(ans)

