import sys

fname = sys.argv[1]

with open(fname) as f:
    prob = f.readlines()

kases = int(prob.pop(0))

for k in range(1, kases + 1):
    choice1 = int(prob.pop(0))
    for i in range(1, 5):
        t = prob.pop(0)
        if i == choice1:
            r1 = set(map(int, t.split(' ')))
    choice2 = int(prob.pop(0))
    for i in range(1, 5):
        t = prob.pop(0)
        if i == choice2:
            r2 = set(map(int, t.split(' ')))

    s = list(r1.intersection(r2))
    if len(s) == 0:
        print("Case #%d: Volunteer cheated!" % k)
    elif len(s) == 1:
        print("Case #%d: %d" % (k, s[0]))
    else:
        print("Case #%d: Bad magician!" % k)
