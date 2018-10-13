for t in range(input()):
    d,n=map(int,raw_input().split())
    time=0
    for i in range(n):
        ki,si=map(int,raw_input().split())
        ti=(float(d)-ki)/si
        #print ti,d-ki
        if ti>time:
            time=ti
    
    speed=d/time
    #print speed,time
    print "Case #"+str(t+1)+": "+"{:.6f}".format(speed)
    
