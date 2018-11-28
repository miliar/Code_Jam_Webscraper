def fun():
    a = int(raw_input())
    mxA = []
    for _ in range(4):
        mxA.append([int(i) for i in raw_input().split(' ')])

    b = int(raw_input())
    mxB = []
    for _ in range(4):
        mxB.append([int(i) for i in raw_input().split(' ')])

    s1 = set(mxA[a - 1])
    s2 = set(mxB[b - 1])
    s = s1.intersection(s2)

    if len(s) > 1:
        return "Bad magician!"
    elif len(s) == 0:
        return "Volunteer cheated!"
    else:
        return list(s)[0]


T = int(raw_input())
for t in range(1, T + 1):
    print "Case #{}: {}".format(t, fun())
