def score(sc, least, diff):
    for i in range(0, 11):
        for j in range(i, max(i+diff+1, 11)):
            for k in range(j, max(j+diff+1, 11)):
                if k >= j >= i >= 0 and i+j+k == sc:
                    if abs(i-j) <= diff and abs(i-k) <= diff and abs(j-k) <= diff and max(i,j,k) >= least:
                        return True
    return False

g = open("output.txt", 'w')
with open("B-large.in") as f:
    N = int(f.readline())
    for i in range(N):
        s = f.readline()
        k = s.split()

        N = int(k[0])
        S = int(k[1])
        p = int(k[2])
        dance = [int(x) for x in k[3:]]
        best = 0
        for sc in dance:
            if score(sc, p, 1):
                best += 1
            elif S > 0 and score(sc, p, 2):
                best += 1
                S -= 1
        out = "Case #%d: %d\n" % (i+1, best)
        g.write(out)

g.close()

