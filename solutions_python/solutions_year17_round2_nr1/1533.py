f = open("input1.in")
tc = int(f.readline())
for i in range(tc):
    p = map(int,f.readline().split())
    d = p[0]
    nh = p[1]
    horses = []
    for j in range(nh):
        l = (map(float,f.readline().split()))
        horses.append((l[0],l[1]))
    horses.sort(reverse=True)
    tm = 0
    xf = (horses[0][0])
    sf = (horses[0][1])
    for k in range(1, nh):
        x = horses[k][0] + tm * horses[k][1]
        if ((horses[k][1]-sf) != 0 and (xf - x)/(horses[k][1]-sf) > 0):
            tempt = (xf - x)/(horses[k][1]-sf)
            tmpx = xf + tempt*sf
            if tmpx >= d:
                xf = x
                sf = horses[k][1]
            else:
                tm += tempt
                xf = tmpx
        else:
            if x < xf:
                xf = x
                sf = horses[k][1]
            else:
                continue

    tm += (d-xf)/(sf)
    print "Case #%d: %s" % (i+1, d/tm) 
