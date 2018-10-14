import sys, itertools

f = open(sys.argv[1], "r")

t = int(f.readline());

for i in range(1, t + 1):
    n = "0" + f.readline().strip()
    m = "".join(sorted(n))
    perms = itertools.permutations(m, len(m))
    s = set(["".join(i) for i in perms])
    combos = sorted(s)
    index = combos.index(n)
    answer = combos[index + 1].lstrip("0")
    print ("Case #{0}: {1}".format(i, answer))

f.close();
