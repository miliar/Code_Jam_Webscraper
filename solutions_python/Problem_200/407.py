def solve(line):
    i = int(line)
    if i < 10:
        return i
    l = i / 10
    r = i % 10
    if l % 10 > r:
        return 10 * solve(l-1) + 9
    else:
        nl = solve(l)
        if nl % 10 == 9:
            return 10 * nl + 9
        else:
            return i

with open("b.in", "r") as fin:
    with open ("b.out", "w") as fout:
        t = int(fin.readline())
        for i in xrange(t):
            res = str(solve(fin.readline()))
            print i+1, res
            fout.write("Case #%d: %s\n" % (i+1, res))
