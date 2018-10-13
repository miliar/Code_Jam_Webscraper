t = int(raw_input())
for i in range(0,t):
    d,n = raw_input().split()
    d = float(d)
    n = float(n)
    times = [ ]
    for j in range(0,int(n)):
        dat  = raw_input().split()
        dat[0] = float(dat[0])
        dat[1] = float(dat[1])
        t = (d-dat[0])/dat[1]
        times.append(t)
    times.sort(reverse = True)
    print "Case #" +str(i+1)+": " +str(d/times[0])
        
