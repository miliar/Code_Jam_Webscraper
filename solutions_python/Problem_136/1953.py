from __future__ import division
def cookies(c,f,x):
    cookies = 0.0
    cps = 2.0
    time = 0.0
    while True:
        #print "stuff"
        #print cookies, cps, time
        time2win = x / cps
        time2farm = c / cps
        time2winwithfarm = x / (cps + f) + time2farm
        #print "times"
        #print time2win, time2farm, time2winwithfarm
        if time2win <= time2farm:
            return time2win + time
        else:
            if time2win <= time2winwithfarm:
                return time2win + time
            else:
                cps = cps + f
                time = time2farm + time

f = open("in.txt","r").read().split("\n")
cases = int(f[0])
for i in range(cases):
    x = f[i+1].split(" ")
    print "Case #" + str(i+1) + ": " + str(cookies(float(x[0]), float(x[1]), float(x[2])))
