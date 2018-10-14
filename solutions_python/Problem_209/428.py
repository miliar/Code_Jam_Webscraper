import math



t = int(input())

for ti in range(1, t + 1):
    # read input
    n, k = [int(s) for s in input().split(" ")]

    sides = []
    bases = []
    both = 0
    bothIndex = -1

    for ni in range(0, n):
        Ri, Hi = [int(s) for s in input().split(" ")]

        side = Hi * 2 * math.pi * Ri
        # sides.append(side)

        top = math.pi * Ri * Ri

        bases.append((ni, side, Ri, top))
        sides.append((ni, side, Ri))

    sortedBases = sorted(bases, key=lambda e: e[2])
    sortedSides = sorted(sides, key=lambda e: e[1], reverse=True)

    sizes = []

    for base in sortedBases:
        pile = 0
        area = base[1] + base[3]
        for side in sortedSides:
            if pile >= k-1:
                break
            if side[0] == base[0] or side[2] > base[3]:
                continue
            area += side[1]
            pile += 1
        sizes.append(area)

    # print(max(sizes))

    print("Case #{}: {}".format(ti, max(sizes)))
    # check format
