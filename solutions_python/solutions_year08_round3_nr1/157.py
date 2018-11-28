no_test_case = input()
for case in range(no_test_case):
    ip = raw_input()
    js = ip.split(" ")
    letters = int(js[0])
    keys = int(js[1])
    alpha = int(js[2])
    s = raw_input()
    l1 = s.split(" ")
    l2 = []
    l3 = [[]]
    for i in l1:
        l2 += [int(i)]
    l2.sort(None,None,True)
    count = 1
    freq = 1
    ans = 0
    for i in range(alpha):
        ans += l2[i] * freq
        #print l2[i],freq,ans
        if(count % (keys) == 0):
            freq += 1
        count += 1
    print "Case #%d: %d"%(case+1,ans)
