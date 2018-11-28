f = open("inp1", "r")
t = int(f.readline())
for tt in range(1,t+1):
    a,b = map(int,f.readline().split())
    p = map(float,f.readline().split())
    for i in range(1,len(p)):
        p[i] = p[i-1]*p[i]
    min = b+2
    if min > b+a+1:
        min = b+a+1
    mi = a
    for i in range(a):
        prob = (b-a+i+i+1)*p[a-i-1] + (i+i+b-a+1+b+1)*(1-p[a-i-1])
        if prob < min:
            min=prob
            mi = i
    print "Case #{0}: {1}".format(tt, min, mi)
