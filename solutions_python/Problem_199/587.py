T = int(input())

inp = [input() for _ in range(T)]

for icase, case in enumerate(inp):
    pancake, k = case.split(' ')
    k = int(k)
    ends = []
    endi = 0
    flip_counter = 0
    fail = False
    for i, p in enumerate(pancake):
        while endi < len(ends):
            if ends[endi] > i:
                break
            endi += 1

        flip = (int(p == '-') + len(ends) - endi) % 2
        flip_counter += flip

        if flip:
            ends.append(i + k)
            if i + k > len(pancake):
                fail = True
    print("Case #{}: {}".format(icase + 1, "IMPOSSIBLE" if fail else flip_counter))
