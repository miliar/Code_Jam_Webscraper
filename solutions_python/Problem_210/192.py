ncase = int(input())

for case in range(1, ncase+1):
    ac, aj = [int(s) for s in input().split(" ")]
    cs = []
    js = []
    if ac > 0:
        for i in range(ac):
            ci, di = [int(s) for s in input().split(" ")]
            cs.append((ci, di))
    if aj > 0:
        for i in range(aj):
            ci, di = [int(s) for s in input().split(" ")]
            js.append((ci, di))
    # print(ac,aj)
    # print(cs)
    # print(js)
    cs.sort(key = lambda x: x[0])
    js.sort(key = lambda x: x[0])

    if ac+aj <= 1:
        ex = 2
    elif ac == 1 and aj == 1:
        ex = 2
    elif ac == 2:
        if cs[1][1] - cs[0][0] <= 720 or cs[1][0] - cs[0][1] >= 720:
            ex = 2
        else:
            ex = 4
    elif aj == 2:
        if js[1][1] - js[0][0] <= 720 or js[1][0] - js[0][1] >= 720:
            ex = 2
        else:
            ex = 4




    print("Case #{}: {}".format(case, ex))

