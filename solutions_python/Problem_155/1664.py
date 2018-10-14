import sys

liste = list()
with open(sys.argv[1]) as f:
    for i, l in enumerate(f.readlines()):
        l = l[:-1]
        if i == 0:
            t = int(l)
        else:
            smax, slist = l.split()
            liste.append((int(smax), [int(x) for x in slist]))

solutions = list()
for s in liste:
    slist = s[1]
    total_invites = 0
    total_present = slist[0]
    for level, level_members in enumerate(slist[1:]):
        level += 1
        if level > total_present:
            level_invites = level - total_present
            total_invites += level_invites
            total_present += level_invites
        total_present += level_members
    solutions.append(total_invites)

for i, s in enumerate(solutions):
    print("Case #{}: {}".format(i + 1, s))
