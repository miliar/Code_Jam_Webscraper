import math

lines = []
with open("B-large.in", 'r') as reader:
   lines = reader.readlines()
t = int(lines[0])
lines = iter(lines[1:])
out = open("2.out", 'w')

def recurse(packs, costs):
    print(packs, costs)
    if [] in packs:
        return 0
    combo = [packs[i][0] for i in range(len(packs))]
    valid = True
    maxp = packs[0][0]/0.9 // costs[0]
    minp = math.ceil(packs[0][0]/1.1 / costs[0])
    if minp > maxp:
        packs[0].pop(0)
        return recurse(packs, costs)
    p = set([0])
    for i in range(1, len(packs)):
        maxc = packs[i][0]/0.9 // costs[i]
        minc = math.ceil(packs[i][0]/1.1 / costs[i])
        if minc > maxc:
            valid = False
            packs[i].pop(0)
            break
        if maxc >= minp and maxp >= minc:
            p.add(i)
            minp = max(minp, minc)
            maxp = min(maxp, maxc)
            continue
        elif minc > maxp:
            valid = False
            for j in p:
                packs[j].pop(0)
            break
        else:
            valid = False
            packs[i].pop(0)
            break
    if valid:
        for i in range(len(packs)):
            packs[i].pop(0)
        return 1 + recurse(packs, costs)
    else:
        return recurse(packs, costs)

for i in range(t):
    tokens = next(lines).split()
    n = int(tokens[0])
    p = int(tokens[1])
    costs = [int(x) for x in next(lines).split()]
    packs = [sorted([int(x) for x in next(lines).split()]) for i in range(n)]
    out.write("Case #" + str(i + 1) + ': ' + str(recurse(packs, costs)) + '\n')

