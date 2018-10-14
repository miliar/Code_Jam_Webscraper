fi = open("D:/Eigene Dokumente/sonstiges/CodeJam/small.txt", 'r')
nr = int(fi.readline())
for case in range(nr):
    pro = fi.readline().split()
    c = float(pro[0])
    f = float(pro[1])
    x = float(pro[2])

    rate = 2.0
    time = c/rate
    if(x < c):
        time = x/rate
    else:
        while (x - c)/rate > c/f:
            #print str((x - c)/rate) + " > " + str(c/(rate + f))
            #print "Time : " + str(time) + " rate: " + str(rate)
            rate += f
            time += c/rate
        time += (x - c)/rate

    print 'Case #' + str(case+1)+ ': ' + str(time)
