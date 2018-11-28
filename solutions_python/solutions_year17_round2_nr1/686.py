filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round 1B\\A\\A-large"

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())



for T in xrange(trials):

    d, n = map(int, fin.readline().split(' '))
    k, s = [], []

    for i in range(n):
        ki, si = map(int, fin.readline().split(' '))
        k.append(ki)
        s.append(si)
        
    times = [float(d-k[i])/float(s[i]) for i in range(n)]
    ans = float(d)/sorted(times)[-1]
    fout.write("Case #%d: %.6f\n" % (T+1, ans))
        
    print "Case #{0} done".format(T+1)
                    
fin.close()
fout.close()