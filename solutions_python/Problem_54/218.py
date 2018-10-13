code = "B-large"

infile = code + ".in"
outfile = code + ".out"

def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a

def solve(line):
    parts = line.split(" ")
    n = int(parts[0])
    m = map(int, parts[1:n+1])
    d = abs(m[1] - m[0])
    for i in range(2, n):
        d = gcd(d, abs(m[i] - m[i-1]))
    r = m[0] % d
    return d - r if r > 0 else 0

lines = [s.strip() for s in open(infile)]
c = int(lines[0])
f = open(outfile, "w")
for i in range(1, c+1):
    r = solve(lines[i])
    print >> f, "Case #%d:" % i, r
f.close()
