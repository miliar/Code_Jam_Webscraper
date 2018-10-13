from math import pi

T = int(input())
PI = 314159265358979323846


def solve():
    n, k = [int(x) for x in input().split()]
    pancakes = []
    for i in range(n):
        r, h = [int(x) for x in input().split()]
        pancakes.append((r, h))
    sides = []
    tops = []
    for r, h in pancakes:
        sides.append(2 * r * h)
        tops.append(r * r)
    usable = []
    for i in range(n):
        top = tops[i]
        side = sides[i]
        usable.append((side, top))
    usable.sort()
    usable.reverse()

    best = 0

    for i in range(n):
        base_top = tops[i]
        base_side = sides[i]
        base = base_top + base_side
        sumtotal = base
        remain = k - 1

        skipped = False

        if remain:
            for side, top in usable:
                if not skipped and side == base_side and top == base_top:
                    skipped = True
                    continue
                if top > tops[i]:
                    continue
                else:
                    sumtotal += side
                    remain -= 1
                    if remain == 0:
                        break

        if not remain:
            best = max(best, sumtotal)

    result = best * PI
    result_base = result // 10**20
    result_div = format(result % 10**20, "020d")
    return "{}.{}".format(result_base, result_div)


for I in range(1, T + 1):
    print("Case #{}: {}".format(I, solve()))
