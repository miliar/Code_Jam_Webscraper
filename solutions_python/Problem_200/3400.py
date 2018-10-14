import fileinput

cases = [c.rstrip() for c in list(fileinput.input())[1:]]
for i, n in enumerate(cases):
    d = [int(c) for c in n]
    v = next((x for x in range(1, len(d)) if d[x] < d[x-1]), None)
    if v is not None:
        m = next((x for x in range(v - 1, 0, -1) if d[x] - 1 >= d[x-1]), 0)
        d[m] -= 1
        d[m+1:] = [9] * (len(d) - m - 1)
    print("Case #{}: {}".format(i + 1, int(''.join(str(x) for x in d))))
