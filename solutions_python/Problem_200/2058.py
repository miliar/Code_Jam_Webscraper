T = int(input())

for casenum in range(1, T+1):
    n = int(input())
    # n, m = [int(s) for s in input().split(" ")] 
    # s = input()

    x = n

    sn = str(x)
    for i in range(len(sn)-1, 0, -1):
        if int(sn[i]) < int(sn[i-1]):
            x = int(sn) - int(sn[i:]) - 1
            sn = str(x)

    print("Case #{}: {}".format(casenum, x))
