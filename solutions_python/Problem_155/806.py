
code = "A-large"

infile = code + ".in"
outfile = code + ".out"

def solve(m, s):
    add = 0
    stand = 0
    for i in xrange(m + 1):
        if stand < i:
            add += i - stand
            stand = i
        stand += s[i]
    return add

with open(infile) as f:
    lines = [s.strip() for s in f]
c = int(lines[0])
with open(outfile, "w") as f:
    for i in range(1, c+1):
        m, s = lines[i].split()
        m = int(m)
        s = map(int, s)
        r = solve(m, s)
        print >> f, "Case #%d:" % i, r
