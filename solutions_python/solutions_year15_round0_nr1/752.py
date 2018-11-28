
for ca in xrange(input()):
    n, s = raw_input().split(' ')
    sn = len(s)
    cnt, ans = 0, 0
    for i in xrange(sn):
        if i > cnt:
            ans += i - cnt
            cnt = i
        cnt += int(s[i])
        
    print "Case #" + str(ca+1) + ": " + str(ans)

        
