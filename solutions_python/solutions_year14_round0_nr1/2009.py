import sys
lines = open(sys.argv[1] + ".in", "rU").read().split("\n")
t, lines = int(lines[0]), lines[1:]

outfile = open(sys.argv[1] + ".out", "w")

for i in range(t):
    first = set(map(int, lines[i*10 + int(lines[i*10])].split()))
    second = set(map(int, lines[i*10 + 5 + int(lines[i*10 + 5])].split()))
    out = list(first.intersection(second))
    if len(out) == 1:
        out = out[0]
    elif not out:
        out = "Volunteer cheated!"
    else:
        out = "Bad magician!"
    print("Case #{}: {}".format(i + 1, out), file=outfile)

