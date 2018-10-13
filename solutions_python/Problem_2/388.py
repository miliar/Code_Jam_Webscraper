def tadd(a, b):
    t = map(int, a.split(":"))
    h = t[0]
    m = t[1]
    m += b
    if m >= 60:
        m %= 60
        h += 1
    s1 = str(h)
    s2 = str(m)
    if len(s1) != 2:
        s1 = "0" + s1
    if len(s2) != 2:
        s2 = "0" + s2

    return s1 + ":" + s2


f = open("B-large.in");
out = open("train-large.out", "w")

N = int(f.readline())

for c in xrange(N):
    T = int(f.readline())
    r = f.readline().split(" ")
    NA = int(r[0])
    NB = int(r[1])

    A = []
    B = []

    for i in xrange(NA):
        A.append(f.readline().strip().split(" "))
    for i in xrange(NB):
        B.append(f.readline().strip().split(" "))

    A.sort()
    B.sort()

    ta = 0
    tb = 0

    while (True):
        if len(B) == 0:
            ta += len(A)
            break
        if len(A) == 0:
            tb += len(B)
            break

        M = []
        X = []
        #Find min of 2
        if cmp(A[0][0], B[0][0]) <= 0:
            M = A
            X = B
            ta += 1
        else:
            M = B
            X = A
            tb += 1

        tr = tadd(M.pop(0)[1], T)
        ff = 1
        while (ff == 1):
            ff = 0
            for w in X:
                if cmp(w[0], tr) >= 0: ## take train back
                    X.remove(w)
                    tr = tadd(w[1], T)
                    Y = X
                    X = M
                    M = Y
                    ff = 1
                    break
                    

    
    out.write("Case #" + str(c+1) + ": " + str(ta) + " " + str(tb) + "\n")    


f.close()
out.flush()
out.close()
