
t = int(raw_input())

ROYGBV = ["R", "O", "Y", "G", "B", "V"]


def find_left(arr, el):
    if el == 0:
        if arr[2][1] >= arr[4][1]:
            return 2
        elif arr[4][1] >= arr[2][1]:
            return 4
    elif el == 2:
        if arr[0][1] >= arr[4][1]:
            return 0
        elif arr[4][1] >= arr[0][1]:
            return 4
    elif el == 4:
        if arr[0][1] >= arr[2][1]:
            return 0
        elif arr[2][1] >= arr[0][1]:
            return 2


for i in xrange(1, t + 1):
    roygbv = [int(s) for s in raw_input().split(" ")]
    n = roygbv.pop(0)
    roygbv = zip(ROYGBV, roygbv)

    max_occur = max(roygbv[0][1] + roygbv[1][1] + roygbv[5][1],
                    roygbv[2][1] + roygbv[1][1] + roygbv[3][1],
                    roygbv[4][1] + roygbv[3][1] + roygbv[5][1])

    if max_occur > (n / 2):
        print "Case #{0}: IMPOSSIBLE".format(i)
        continue

    res = []
    cur = 0
    while n > 0:
        nxt = find_left(roygbv, cur)
        roygbv[nxt] = (roygbv[nxt][0], roygbv[nxt][1] - 1)
        n -= 1
        res.append(roygbv[nxt][0])
        cur = nxt

    if res[-1] == res[0]:
        res[-1], res[-2] = res[-2], res[-1]

    print "Case #{}: {}".format(i, "".join(res))
