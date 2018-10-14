
import random

with open('in.txt') as fp:
    T = int(fp.readline())
    for t in range(1, T + 1):
        N = T = int(fp.readline())
        blocks_a = sorted(list(map(float, fp.readline().split())))
        blocks_b = sorted(list(map(float, fp.readline().split())))

        dwar_won = 0

        blocks_a_c = list(blocks_a)
        blocks_b_c = list(blocks_b)

        for i in range(N):
            b = blocks_b_c.pop(0)

            for n, a in enumerate(blocks_a_c):
                if a > b:
                    break
                else:
                    a = None
                    n = 0

            a = blocks_a_c.pop(n)

            if a > b:
                dwar_won += 1
            # max_b = max(blocks_b_c)

            # print("tell", max_b - 0.00001)
            # print(a, b, a > b)
            # blocks_b_c.remove(max_b)


        war_won = 0
        for i in range(N):
            a = blocks_a.pop(0)
            for n, b in enumerate(blocks_b):
                if b > a:
                    break
                else:
                    b = None
                    n = 0
            if b is None:
                war_won += 1
            blocks_b.pop(n)

        print("Case #%d: %d %d" % (t, dwar_won, war_won))


