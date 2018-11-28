tc = int(input())

for t in range(tc):
    n = int(input())

    tmp = 0
    j = 0
    for i in range(20, -1, -1):
        while True:
            new_tmp = tmp + (10 ** i - 1) // 9
            if j < 9 and new_tmp <= n:
                tmp = new_tmp
                j += 1
            else:
                break

    print("Case #%d: %d" % (t+1, tmp))
