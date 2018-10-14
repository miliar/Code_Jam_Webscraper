ips = input()
for w in range(ips):
    n = input()
    nos = raw_input()
    a,b = nos.split(" ")
    depart_a = []
    depart_b = []
    arriv_a = []
    arriv_b = []
    for i in range(int(a)):
        time1 = raw_input()
        arrv,depart = time1.split(" ")
        marrv,sarrv = arrv.split(":")
        t1 = int(marrv) * 60 + int(sarrv)
        depart_a += [t1]
        mdepart,sdepart = depart.split(":")
        t2 = int(mdepart) *60 + int(sdepart) + n
        arriv_b += [t2]
    for i in range(int(b)):
        time1 = raw_input()
        arrv,depart = time1.split(" ")
        marrv,sarrv = arrv.split(":")
        t1 = int(marrv) * 60 + int(sarrv)
        depart_b += [t1]
        mdepart,sdepart = depart.split(":")
        t2 = int(mdepart) *60+ int(sdepart) + n
        arriv_a += [t2]
    ansa = int(a)
    ansb = int(b)
    arriv_a.sort()
    arriv_b.sort()
    depart_a.sort()
    depart_b.sort()
    for arrival_to_b in arriv_b:
            for k1 in range(len(depart_b)):
                if(depart_b[k1] >= arrival_to_b):
                    del depart_b[k1]
                    ansb -= 1
                    break
##        if(arrival_to_b >= min(depart_b) and arrival_to_b <= max(depart_b)):
##            ansb -= 1
    for arrival_to_a in arriv_a:
        for k1 in range(len(depart_a)):
            if(depart_a[k1] >= arrival_to_a):
                del depart_a[k1]
                ansa -= 1
                break
##        if(arrival_to_a >= min(depart_a) and arrival_to_a <= max(depart_a)):
##             ansa -= 1
           #  print ("%d:%d")%((arrival_to_a-n)/60,arrival_to_a - (((arrival_to_a-n)/60)*60))
    print "Case #%d: %d %d"%(w+1,ansa,ansb)

        
        
