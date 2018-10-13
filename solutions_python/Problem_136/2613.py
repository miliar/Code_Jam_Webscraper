t = int(raw_input())+1
for case in range(1,t):
    data = raw_input().split()
    C = float(data[0])
    F = float(data[1])
    X = float(data[2])
    rate = 2.0
    s = 0.0
    cookies = 0
    while cookies<X:
        d = (C-cookies)/rate
        cookies = cookies + d*rate
        s = s + d
        # if buy
        r1 = rate+F
        c1 = cookies-C
        #time to win
        x1 = (X-c1)/r1
        x2 = (X-cookies)/rate
        if x1<x2:
            #quicker with buy
            rate = rate+F
            cookies = c1
        else:
            s = s+x2
            break
        
    print "Case #%s: %0.7f" % (case, s)
