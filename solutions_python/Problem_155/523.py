# Small & Large

fin = open("largeA.txt", "r")
fout = open("largeA.out", "w+")

T = int(fin.readline())

for n in xrange(T):
    data = fin.readline().split()
    smax = int(data[0])
    s = []
    for i in xrange(smax+1):
        s.append(int(data[1][i]))
    
    stand = 0
    ans = 0
    for i in xrange(smax+1):
        if stand < i:
            stand += 1
            ans += 1
        stand += s[i]
    print "Case #%i: %i" %(n+1, ans)
    fout.write("Case #%i: %i\n" %(n+1, ans))
