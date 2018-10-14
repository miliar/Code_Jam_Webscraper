import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    line = sys.stdin.readline()
    d, n = line.split()
    d = int(d)   
    n = int(n)

    maxt = -1
    for i in xrange(n):
        line = sys.stdin.readline()
        k, s = line.split()
        k = int(k)
        s = int(s)


        #if t == 34:
        #    print line
        time = (d - k)  / float(s)
        maxt = max(time, maxt)


    y = d/maxt
    print("Case #%d: %f" % (t+1, y))

