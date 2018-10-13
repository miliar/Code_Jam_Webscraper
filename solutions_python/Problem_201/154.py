x = int(input())

# import time

for case in range(1, x + 1):
    # t0 = time.time()
    n, k = [int(s) for s in input().split(" ")]
    i = 0
    j = 0
    while (2**i <= k):
        i += 1
    while (2**j <= n):
        j += 1
    # print(i, j, 2**i-1, 2**j-1)

    defect = 2**j-1 - n
    parts = 2**(i-1)
    no_defect = int(2**j / parts)
    # print(n, parts, no_defect)
    # print(parts, defect)

    import math
    ave_defect = math.floor(defect / parts)
    # print("ave_defect", ave_defect)

    spaces = ([no_defect - ave_defect - 2 for i in range(defect % parts)] +
              [no_defect - ave_defect - 1 for i in range(parts - defect%parts)])
    # print(n, parts, no_defect)
    # print(spaces)

    y = 0
    z = 0

    rank = k - 2**(i-1)
    t = spaces[-rank-1]
    # print(t)
    if t is 0:
        y, z = 0, 0
    elif t % 2 is 0:
        y, z = t/2, t/2-1
    else:
        y, z = (t-1)/2, (t-1)/2
    # print(spaces, y, z)

    # t1 = time.time()
    # print(t1-t0)
    print("Case #{}: {} {}".format(case, int(y), int(z)))

