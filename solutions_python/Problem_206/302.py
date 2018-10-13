fin = open('A-large.in')
fout = open('outputl.txt', 'w')
T = int(fin.readline())
for tt in range(T):
    D, N = map(int, fin.readline().split(' '))
    H = []
    ti = 0
    for n in range(N):
        K, S = map(float, fin.readline().split(' '))
        ti = max(ti, (D - K) / S)
    fout.write("Case #%s: %.6f\n" % (tt + 1, float(D) / ti))
fin.close()
fout.close()