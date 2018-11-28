inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    args=list(((inp.readline()).rstrip()).split())
    D = int(args[0])
    N = int(args[1])
    km = []
    sp = []
    minh = -1
    for j in range(N):
        temp = list(((inp.readline()).rstrip()).split())
        ki = int(temp[0])
        si = int(temp[1])
        t=(D - ki)/si
        if t>minh:
            minh = t
        km.append(ki)
        sp.append(si)
    tt = D/minh
    ans = tt - (tt%0.000001)
    anss = "{0:.6f}".format(ans)
    out.write("Case #" + str(i+1) + ": "+anss+"\n")