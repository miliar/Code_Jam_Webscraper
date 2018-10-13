

fin = open("a22.in")
fout = open("1.out","w")
c = int(fin.readline())
res = 0
for i in xrange(c):
    ts = map(int,fin.readline().split())
    p=ts[0]
    k=ts[1]
    l=ts[2]

    freq = map( int, fin.readline().split())
    freq.sort()
    freq.reverse()
    res = 0
    for j in xrange(l):
        res = res + freq[j] * ((j / k) + 1)
    fout.write( "Case #%d: %d\n" %(i+1, res))
    
fout.close()
