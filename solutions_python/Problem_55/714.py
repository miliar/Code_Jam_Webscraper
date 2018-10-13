"""
Google Code Jam 2010
Qualification Round
Challenge: C. Theme Park

By Marcel Rodrigues

Code for Python 2.x
"""

filename = "C-small-attempt0"

inpath = filename + ".in"
outpath = filename + ".out"

infile = open(inpath, "r")
outfile = open(outpath, "w")

ncases = int(infile.readline().rstrip())

for case in range(ncases):
    x = infile.readline().rstrip().split()
    x = [int(i) for i in x]
    R, k, N = x
    q = infile.readline().rstrip().split()
    q = [int(i) for i in q]
    c = 0
    for ride in range(R):
        b = []
        g = 0
        v = k
        while q[g] <= v:
            v -= q[g]
            b.append(q[g])
            g += 1
            if g == N:
                break
        c += sum(b)
        q = q[g:] + q[:g]
    outfile.write("Case #%d: %d\n" % (case + 1, c))

infile.close()
outfile.close()
