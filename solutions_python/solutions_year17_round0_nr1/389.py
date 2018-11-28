def solve(line):
    parts = line.split()
    l = list(parts[0])
    k = int(parts[1])
    n = len(l)
    c = 0
    for i in xrange(n):
        if l[i] == "-":
            if i + k > n:
                return "IMPOSSIBLE"
            c += 1
            for j in xrange(k):
                if l[i+j] == "+":
                    l[i+j] = "-"
                else:
                    l[i+j] = "+"
    return c

with open("in.txt", "r") as fin:
    with open ("out.txt", "w") as fout:
        t = int(fin.readline())
        for i in xrange(t):
            res = str(solve(fin.readline()))
            print i+1, res
            fout.write("Case #%d: %s\n" % (i+1, res))
