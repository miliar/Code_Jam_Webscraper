import sys

fname = sys.argv[1]
with open(fname) as f:
    T = int(f.readline())
    for i in range(T):
        C,F,X = tuple(map(lambda x:float(x),f.readline().split()))
        time = 0
        rate = 2
        waittime = X/rate
        buytime = C/rate + X/(rate+F)
        while waittime > buytime:
            time = time+C/rate
            rate = rate+F
            waittime = X/rate
            buytime = C/rate + X/(rate+F)
        time = time + X/rate
        print("Case #%s: %s"%(i+1,time))
    
