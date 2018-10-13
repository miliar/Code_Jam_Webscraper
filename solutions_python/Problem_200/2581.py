import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    line = line.strip()


    ints = [int(c) for c in line]

    for k in reversed(range(1,len(ints))):
        if tuple(sorted(ints)) == tuple(ints):
            break
        if ints[k] == 9:
            continue

        ints[k] = 9
        ints[k-1] = ints[k-1] -1
        for j in reversed(range(k)):
            if ints[j] < 0:
                ints[j] = 9
                ints[j-1] = ints[j-1] -1

    while ints[0] == 0:
        ints = ints[1:]

    print("Case #{}: {}".format(i, ''.join(str(c) for c in ints)))
            