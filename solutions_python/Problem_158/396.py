def solve(X, R, C):
    if X == 1:
        return 0
    if X == 2:
        return R * C % 2
    if X == 3:
        if min(R, C) == 1 or R * C % 3 != 0:
            return 1
        return 0
    if X == 4:
        if min(R, C) <= 2 or R * C % 4 != 0:
            return 1
        return 0

with open("input.txt") as fin, open("output.txt", 'w') as fout:
    t = int(fin.readline())
    for i in range(1, t + 1):
        X, R, C = [int(i) for i in fin.readline().split()]
        name = ["GABRIEL", "RICHARD"][solve(X, R, C)]
        print("Case #{0}: {1}".format(i, name), file=fout)