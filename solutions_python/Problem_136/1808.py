def t(n,X,C,F):
    n = 0
    tc = 0
    while 1:
        if X/(2+n*F) < X/(2+n*F+F) + C/(2+n*F) :
            return X/(2+n*F) + tc
        else:
            tc = tc + C/(2+n*F)
            n = n + 1






f = open("C:/Users/tadeo/Downloads/B-large.in","r")
fw = open("C:/Users/tadeo/Downloads/B.out", "w")
T = int(f.readline())
for i in range(T):
    print 100.0*i/T
    a = [float(x) for x in f.readline().split(" ")]
    C = a[0]
    F = a[1]
    X = a[2]
    s = str(t(0,X,C,F))
    fw.write("Case #"+str(1+i)+": "+s+"\n")
f.close()
fw.close()

