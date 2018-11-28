with open("B-large.in", "r") as f:
    num_case = int(f.readline())
    #lst.append(f.readline().split())

    
    
    for n in range(1, num_case + 1):
        cookie = (f.readline().split())
        #print(float(cookie[0]), cookie[1], cookie[2])
        #500.0(C) 4.0(F) 2000.0(X) 

        numCookie = 2
        ltime = 0
        btime = 0
        stime = 0
        
        while(1):

            ltime = stime + float(cookie[2])/numCookie                         
            stime = stime + float(cookie[0])/numCookie
            numCookie =  numCookie + float(cookie[1])
            btime = stime + float(cookie[2])/numCookie 

            if(btime > ltime):
                break
        if(btime > ltime):
            print ("Case #%d: %.7f" %(n, ltime))
        else:
            print ("Case #%d: %.7f" %(n, btime))



        
    
