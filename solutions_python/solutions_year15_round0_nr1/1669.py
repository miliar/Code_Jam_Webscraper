n=raw_input()
for i in xrange(1,int(n)+1):
    s=raw_input().split()
    Smax = int(s[0])
    eachlevel = s[1]
    count = 0
    ans = 0
    for j in xrange(0,Smax):
        if int(eachlevel[j]) != 0:
            count += int(eachlevel[j])
        else:
            if count<j+1:
                ans += 1
                count += 1
       # print count
    print 'Case #'+str(i)+': '+str(ans)
