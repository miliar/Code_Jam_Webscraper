import sys
lines = open(sys.argv[1] + ".in", "rU").read().split("\n")
t, lines = int(lines[0]), lines[1:]

outfile = open(sys.argv[1] + ".out", "w")

for i in range(t):
    n, levels = lines[i].split()
    levels = list(map(int, list(levels)))
    out = upto = 0
    for j, num in enumerate(levels):
        if upto < j:
            out += j - upto
            upto = j
        upto += num
    print("Case #{}: {}".format(i + 1, out), file=outfile)

