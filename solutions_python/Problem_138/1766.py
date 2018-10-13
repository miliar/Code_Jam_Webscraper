t = input()
k = 0
while t > 0:
    t -= 1
    k += 1
    nor, dec = 0, 0
    knor, kdec = 0,0
    n = input()
    na = [float(i) for i in raw_input().split()]
    ke = [float(i) for i in raw_input().split()]
    na.sort(reverse=True)
    ke.sort(reverse=True)
    # normal method
    sn, en = 0, len(na)-1
    sk,ek = 0, len(ke)-1
    while  (nor+knor) < n: 
        if na[sn] > ke[sk]:
            nor += 1
            sn += 1
        else:
            knor+=1 
            sn += 1
            sk += 1
    sn = n-1
    sk = n-1
    while (dec + kdec) < n:
       if na[sn] < ke[sk]:
          kdec += 1
          sn -= 1
       else:
          dec += 1
          sk -= 1
          sn-=1
    print "Case #%d: %d %d"%(k, dec, nor)
    
