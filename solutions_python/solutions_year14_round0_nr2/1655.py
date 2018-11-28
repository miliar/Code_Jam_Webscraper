def bestTime(c, f, n, x, bt):
    nr = 2.0
    t = 0.0
    n += 1
    i = 0
    while i < n:
        t += (c/nr)
        nr += f
        i += 1
    t += (x/nr)
    if t < bt :
        bt = t
        return bestTime(c,f,n,x,bt)
    return bt
    
fi = open("a.txt", "r", 0)
t = int(fi.readline())
i = 0
while i < t:
    a = fi.readline().split(' ')
    c = float(a[0])
    f = float(a[1])
    x = float(a[2])
    bt = x/2.0
    bt = bestTime(c, f, 0, x, bt)
    print "Case #" + str(i+1) + ": " + str(bt)
    i += 1  