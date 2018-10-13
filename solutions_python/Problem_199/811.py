t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    p, f = [s for s in input().split(" ")]
    f = int(f)
    p = [True if c == '+' else False for c in p]

    index = 0
    count = 0

    while len(p) - (index + f) >= 0:
        if not p[index]:
            for k in range(f):
                p[index + k] = not p[index + k]
            count += 1

        index += 1

    result = ""
    if sum(p) == len(p):
        result = str(count)
    else:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, result))
    # check out .format's specification for more formatting options
