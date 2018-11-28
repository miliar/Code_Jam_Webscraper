with open("B-large.in") as f:
    T = f.readline().rstrip('\n');
    #print T
    for ii in range(int(T)):
        C, F, X = f.readline().rstrip('\n').split(' ')
        #print C, F, X
        count = 0
        rate = 2.0
        time = 0.0
        while True:
            if (float(X)-count < float(C)):
                time += (float(X)-count)/rate
                print "Case #%s: %.7f" %(ii+1, time)
                break
            time += float(C)/rate
            count += float(C)
            if (count >= float(X)):
                print "Case #%s: %.7f" %(ii+1, time)
                break
            time1 = (float(X)-float(count))/rate
            time2 = float(X)/(rate + float(F))
            if time1 < time2:
                continue
            else:
                count = 0
                rate += float(F)
            #print time1, time2
