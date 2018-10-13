
code = "B-large"

infile = code + ".in"
outfile = code + ".out"

def solve(line):
    parts = map(int, line.split())
    n, s, p = parts[:3]
    t = parts[3:3+n]
    m = 2*max(p-2, 0) + p
    M = 2*max(p-1, 0) + p
    good, maybe = 0, 0
    for x in t:
        if x >= M:
            good += 1
        elif x >= m:
            maybe += 1
    good += min(maybe, s)
    return good

lines = [s.strip() for s in open(infile)]
c = int(lines[0])
f = open(outfile, "w")
for i in range(1, c+1):
    r = solve(lines[i])
    print >> f, "Case #%d:" % i, r
f.close()
