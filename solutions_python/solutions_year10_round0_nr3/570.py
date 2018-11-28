fin = open("C-small-attempt0.in", "r")
fout = open("C-small-attempt0.out", "w")

T = int(fin.readline())

for t in xrange(T):
    R, k, N = [int(i) for i in fin.readline().split()]
    g = [int(i) for i in fin.readline().split()]
    profit = 0
    start = 0
    for r in xrange(R):
        fullness = 0
        gone = 0
        while fullness + g[start] <= k and gone < N:
            fullness += g[start]
            profit += g[start]
            start = (start + 1) % N
            gone += 1
    #print "Case #%i: %i" % (t + 1, profit)
    fout.write("Case #%i: %i\n" % (t + 1, profit))

fin.close()
fout.close()

print "done"
