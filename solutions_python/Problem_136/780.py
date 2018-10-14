cas = int(raw_input().strip())

for cc in range(1,cas+1):
    inp = raw_input().strip().split()
    c = float(inp[0])
    f = float(inp[1])
    x = float(inp[2])

    ans = x/2.0

    time = [0]
    tmp = 0
    i = 0
    while(True):
        tmp = time[i] + c/(i*f+2.0)
        time.append(tmp)
        i += 1
        if(time[i] + x/(i*f+2.0) > time[i-1] + x/((i-1)*f+2.0)):
            break
        #print '********',
        #print tmp

    #print time

    for i in range(len(time)):
        ans = min(time[i]+(x/(i*f+2)),ans)
    
    print 'Case #' + str(cc) + ': ' + str(ans)
