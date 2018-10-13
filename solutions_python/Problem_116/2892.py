
s = open("in.txt", "r").read()

def check(a):
    l = len(set(a))
    if l == 1 and a[0] != ".":
        return a[0]

    if l == 2:
        if a.count("X") == 3 and a.count("T") == 1:
            return "X"

        if a.count("O") == 3 and a.count("T") == 1:
            return "O"

    return False

lines = s.split("\n\n")

n_cases = lines[0][:1]

lines[0] = lines[0][3:]


cases = []
for line in lines:
    if line:
        cases.append(line.splitlines())


print cases

f = open("out.txt", "w")


for i in xrange(len(cases)):
    q = 0
    for c in xrange(4):
        if check(cases[i][c]):
            f.write("Case #%d: %s won" % ((i+1), check(cases[i][c])) + "\n")
            q = 1

        if check([j[c] for j in cases[i]]):
            f.write("Case #%d: %s won" % ((i+1), check([j[c] for j in cases[i]])) + "\n")
            q = 1
    if q:
        continue

    if check([cases[i][k][k] for k in xrange(4)]):
        f.write("Case #%d: %s won" % ((i+1), check([cases[i][k][k] for k in xrange(4)])) + "\n")
        continue

    if check([cases[i][k][-(k+1)] for k in xrange(4)]):
        f.write("Case #%d: %s won" % ((i+1), check([cases[i][k][-(k+1)] for k in xrange(4)])) + "\n")
        continue

    if [cases[i][t][r] for t in xrange(4) for r in xrange(4)].count(".") == 0:
        f.write("Case #%d: Draw" % (i+1) + "\n")
        continue

    f.write("Case #%d: Game has not completed" % (i+1) + "\n")


f.close()