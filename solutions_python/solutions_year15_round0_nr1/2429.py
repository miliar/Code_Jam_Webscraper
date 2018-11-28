n = int(raw_input())
for x in range(n):
    smax,s = raw_input().split()
    slen = int(smax)
    au = 0
    total = 0
    for i in range(slen+1):
        if int(s[i]) > 0:
            #print i,s[i],total
            addp=0
            if total < i:
                addp = i - total
                au+=addp
                #print 'au ',au
                
            total += int(s[i]) + addp
            
    print "Case #%d: %d" % (x+1,au)

