t = int(raw_input())

def time(c, x, f, rate, time, cookie):
    t = float(c/rate)
    
    

for ab in xrange(t):
    inp = raw_input()
    c, f, x = map(float, inp.split())

    time = 0.0
    cookiecount = 0
    rate = 2.0
    while True:
        t = float(c/rate)
        t1 = float(x/(rate+f)) + float(c/rate)
        t2 = float((x-c)/rate) + float(c/rate)
        if t1 < t2:
            rate += f
            cookiecount = 0
            time += t
        else:
            cookiecount = c
            time += t
            break

    time += float(x-cookiecount)/(rate)
    print "Case #" + str(ab+1) + ": " + str(time)
            

