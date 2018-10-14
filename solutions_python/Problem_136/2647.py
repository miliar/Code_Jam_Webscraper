fin = open("input", "r")
fout = open("output", "w")

t = int(fin.readline())

for test in range(t):
    c,f,x = [float(x) for x in fin.readline().split(" ")]

    s = 0.0
    min_T = None
    n = -1
    T = x/2.0

    while min_T == None or T < min_T:
        min_T = T

        n += 1
        r = x / (2+(n+1)*f)
        s += c / (2+n*f)
        T = s + r
        # print(n,s,r,T, min_T)

    fout.write("Case #%d: %0.7f\n" % (test+1, min_T))

fin.close()
fout.close()
