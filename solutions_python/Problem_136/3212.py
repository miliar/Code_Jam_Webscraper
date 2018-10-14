import numpy as np

fl = open('B-large.in','r')
fr = open('2.result','w')

r = int(fl.readline())
for i in range(1,r+1):
    l = np.fromstring(fl.readline(), dtype=float, sep=' ')
    c = l[0]
    f = l[1]
    x = l[2]

    #count = 0.0
    rate = 2.0
    time = 0.0

    #while (x-count)/rate + time > (c-count)/rate + (x-count)/(rate+f) + time:
    while (x)/rate > (c)/rate + (x)/(rate+f):
        time+= (c/rate)
        #time+= (c-count)/rate
        rate+=f
    #print("Case #%i: %f" % (i, (x-count)/rate + time ))
    fr.write("Case #%i: %f\n" % (i, (x)/rate + time ))

