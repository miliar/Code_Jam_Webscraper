import math

T = int(input())
for i in range(1, T + 1):
    [N, P] = [int(x) for x in input().split(" ")]
    groups = [int(x) for x in input().split(" ")]

    result = 0

    temp = []
    for idx in range(N):
        if groups[idx] % P != 0:
            temp.append(groups[idx] % P)
        else:
            result += 1
    groups = temp
    groups.sort()


    new = []
    for j in range(1, P):
        new.append(groups.count(j))

    if P == 2:
        result += math.ceil(new[0] / 2)
    elif P == 3:
        mi = min(new[0], new[1])
        result += mi
        ma = max(new[0], new[1])
        ma = ma - mi
        result += math.ceil(ma / 3)
    elif P == 4:
        mi = min(new[0], new[2])
        result += mi
        ptl = max(new[0], new[2])
        result += math.ceil(new[1] / 2)
        ps = new[1] % 2
        if ps == 1:
            if ptl >= 2:
                ptl -= 2
                result += math.ceil(ptl / 4)
        else:
            result += math.ceil(ptl / 4)

    print("Case #{}: {}".format(i, result))
