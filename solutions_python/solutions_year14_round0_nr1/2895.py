t = int(input())
for i in range(t):
    l1 = int(input()) - 1
    case1 = [[int(j) for j in input().split()] for k in range(4)]
    l2 = int(input()) - 1
    case2 = [[int(j) for j in input().split()] for k in range(4)]
    v1 = case1[l1]
    v2 = case2[l2]
    cnt = 0
    res = float("inf")
    for j in v1:
        if j in v2:
            cnt += 1
            res = j
    if cnt == 0:
        print("Case #", i + 1, ": Volunteer cheated!", sep="")
    elif cnt == 1:
        print("Case #", i + 1, ": ", res, sep="")
    else:
        print("Case #", i + 1, ": Bad magician!", sep="")