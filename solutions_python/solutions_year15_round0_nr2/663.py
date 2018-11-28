
code = "B-large"

infile = code + ".in"
outfile = code + ".out"

def time(p, m):
    return sum((pi - 1) // m for pi in p) + m

def solve(p):
    return min(time(p, m) for m in xrange(1, max(p) + 1))

with open(infile) as f:
    lines = [s.strip() for s in f]
c = int(lines[0])
with open(outfile, "w") as f:
    lineno = 1
    for i in range(1, c+1):
        d = int(lines[lineno])
        p = map(int, lines[lineno+1].split())
        r = solve(p[:d])
        lineno += 2
        print >> f, "Case #%d:" % i, r
