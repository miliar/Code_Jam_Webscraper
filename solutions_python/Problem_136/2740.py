t = int(raw_input())
for i in range(t):
    line = raw_input()
    c,f,x = [float(x) for x in line.split(' ')]

    perSec = 2.0
    time = 0
    while True:
        nextFarm = c / float(perSec) + x / float(perSec+ f)
        t = x / float(perSec)
        if (t <= nextFarm):
            time += t
            break
        else:
            time += c/float(perSec)
            perSec += f

    print "Case #%d: %f" % (i+1, time)
