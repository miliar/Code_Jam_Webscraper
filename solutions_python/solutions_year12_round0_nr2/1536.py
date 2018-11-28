#inpath = "in.txt"
inpath = "B-large.in"
outpath = "out.txt"

single = lambda f, c: c(f.readline().strip("\n"))
multi = lambda f, c: [c(s) for s in f.readline().split()]
case = lambda f, n, c: f.write("Case #%d: %s\n" % (n, " ".join(map(str, c))))

infile = open(inpath, "r")
outfile = open(outpath, "w")

N = single(infile, int)
for i in range(N):
    T = multi(infile, int)
    N = T.pop(0)
    S = T.pop(0)
    p = T.pop(0)
    p3 = 3 * p
    y = 0
    for t in T:
        if t == 0:
            if p == 0:
                y += 1
        elif t <= p3 - 5:
            continue
        elif t <= p3 - 3:
            if S:
                y += 1
                S -= 1
        else:
            y += 1

    case(outfile, i + 1, [y])

infile.close()
outfile.close()
