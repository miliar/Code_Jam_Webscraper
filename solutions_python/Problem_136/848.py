f = open("data.txt", 'r')
g = open("data1.txt", 'w')
T = int(f.readline())

for i in range(1, T+1):
    (C, F, X) = [float(x) for x in f.readline().split()]
    k = 0
    time = 0.0
    while (X-C)*(2 + (k+1)*F) > (2 + k*F)*X:
        k += 1
        time += C/(2.0 + (k-1)*F)
    time += X/(2.0 + k*F)
    g.write("Case #%d: %.7f\n" % (i, time))
f.close()
g.close()