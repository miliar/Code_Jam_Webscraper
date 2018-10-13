str = "B-large.in"
fo = open(str, "r");
T = int(fo.readline());
for i in range(T):
    info = fo.readline().strip().split(" ")
    C = float(info[0])
    F = float(info[1])
    X = float(info[2])
    if X * F <= C * F + 2 * C :
        print "Case #%d: %f" % (i+1, X/2)
    else:
        n = int((X * F - 2 * C) / (F * C))
        time = 0.0
        for a in range(n):
            time += C / (a * F + 2)
        time += X / (n * F + 2)
        print "Case #%d: %f" % (i+1, time)
