i = open('a.in')

test_cases = int(i.readline())

for t in range(1, test_cases+1):
    se_c = int(i.readline())
    se = []
    for c in range(se_c): se.append(i.readline().strip())

    cur_se = se[:]

    kw_c = int(i.readline())
    sw_c = 0

    for c in range(kw_c):
        kw = i.readline().strip()

        #print cur_se
        #print kw

        if kw in cur_se:
            #print 'remove', kw
            cur_se.remove(kw)
        
        if not cur_se:
            #print 'switch'
            sw_c += 1
            cur_se = se[:]
            cur_se.remove(kw)


    print "Case #%d: %d" % (t, sw_c)
    #print
