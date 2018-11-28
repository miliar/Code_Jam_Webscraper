import sys

f = open(sys.argv[1])
t = 1
f.readline()
l = f.readline()
while l != "":
    n,v,x = l.split()
    n,v,x = int(n),float(v),float(x)
    #sources = [[ float(i) for i in f.readline().split() ] for j in range(n)]
    output = "IMPOSSIBLE"
    if n == 2:
        r1,x1 = [float(i) for i in f.readline().split()]
        r2,x2 = [float(i) for i in f.readline().split()]
        if x1 == x2:
            if x1 == x:
                output = "{:.6f}".format(v / (r1+r2))
        else:
            t1 = (v*x-v*x2) / (r1*x1-r1*x2)
            t2 = (v*x-v*x1) / (r2*x2 - r2*x1)
            if t1 >= 0 and t2 >= 0:
                output = "{:.6f}".format(max(t1,t2))
            #print t1, t2
    elif n == 1:
        r1,x1 = [float(i) for i in f.readline().split()]
        if x1 == x:
            output = "{:.6f}".format(v / r1)
    else:
        sources = [f.readline() for j in range(n)]

    print "Case #{}: {}".format(t,output)
    t += 1
    l = f.readline()
