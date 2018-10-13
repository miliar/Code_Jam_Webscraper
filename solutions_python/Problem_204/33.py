inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "
    n, p = [int(x) for x in inf.readline().split()]
    rs = [int(x) for x in inf.readline().split()]
    ps = []
    for i in range(n):
        ps.append(sorted([int(x) for x in inf.readline().split()]))

    idx = [0] * n
    kits = 0
    done = False
    while not done and idx[0] < p:
        amount0 = ps[0][idx[0]]
        maxs = (amount0 * 100) // (90 * rs[0])
        mins = ((amount0 * 100) + (110 * rs[0]) - 1) // (110 * rs[0])
        # print(amount0, mins, maxs)
        fail = False
        if mins > maxs:
            fail = True
        for i in range(1, n):
            while idx[i] < p and ps[i][idx[i]] < (mins * rs[i] * 90) // 100:
                idx[i] += 1
            if idx[i] >= p:
                done = True
                fail = True
                break
            if ps[i][idx[i]] > (maxs * rs[i] * 110) // 100:
                fail = True
                break
        if not fail:
            for i in range(1, n):
                idx[i] += 1
                if idx[i] >= p:
                    done = True
            kits += 1
        idx[0] += 1

    rstr += str(kits)
    print(rstr)
    outf.write(rstr + '\n')
