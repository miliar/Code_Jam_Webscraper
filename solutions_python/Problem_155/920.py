for t in range(input()):
    s, a = raw_input().split(' ')
    smax = int(s)
    arr = [int(d) for d in a]
    csum = []
    csum.append(arr[0])
    direct = True
    fcnt = 0
    np = False
    
    for i in range(1,len(arr)):
        lcnt = 0
        if csum[i-1] < i:
            direct = False
            lcnt = abs(csum[i-1] - i)
            fcnt = fcnt + lcnt
            #print csum
            #print lcnt
            # for j in range(i-1,-1,-1):
            #     if csum[i-1] + lcnt <= 9:
            #         csum[i-1] += lcnt
            #         lcnt = 0
            #         break
            #     else:
            #         lcnt = lcnt - (9 - csum[i-1])
            #         csum[i-1] = 9
            # if lcnt > 0:
            #     np = True
            #     break
        csum.append(arr[i]+csum[i-1]+lcnt)           
            
    if direct==True:
        print "Case #%d: 0" % (t+1)
    else:
        if np==True:
            print "Case #%d: -1" % (t+1)
        else:
            print ("Case #%d: " % (t+1)) + str(fcnt)