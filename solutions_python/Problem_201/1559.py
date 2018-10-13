import math
from pip._vendor.distlib.compat import raw_input


def helper(n):
    if n % 2 == 0:
        temp = [(n/2)-1, n/2]
    else:
        temp = [(n-1)/2, (n-1)/2]
    return temp


def stall(n, k):

    if k == 1:
        loc = helper(n)
        return int(loc[0]), int(loc[1])
    count = int(math.log(k , 2))
    n = helper(n)
    idx = [1, 1]

    for j in range(count-1):
        if n[0] % 2 == 0:
            if n[0] != n[1]:
                n = helper(n[0])
                if n[0] > n[1]:
                    idx = [idx[0], idx[1]*2 + idx[0]]
                else:
                    idx = [idx[0], idx[1]*2 + idx[0]]
            else:
                n = helper(n[0])
                idx = [idx[0]*2, idx[1]*2]
        else:
            if n[0] != n[1]:
                n = helper(n[1])
                if n[0] > n[1]:
                    idx = [idx[0], idx[1]*2 + idx[0]]
                else:
                    idx = [idx[0] * 2 + idx[1], idx[1]]
            else:
                n = helper(n[1])
                idx = [idx[0] * 2, idx[1] * 2]

    rank = k - 2**count + 1

    if n[0] > n[1]:
        if rank > idx[0] and n[1] != 0:
            loc = n[1]
        else:
            loc = n[0]
    else:
        if rank > idx[1] and n[0] != 0:
            loc = n[0]
        else:
            loc = n[1]

    loc = helper(loc)
    return int(loc[0]), int(loc[1])


if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t+1):
        n, k = [int(x) for x in raw_input().split()]
        c1, c2 = stall(n, k)
        #print("Case #{}: {} {}".format(i, c2, c1))
        print("Case #{}: {} {}".format(i, c2, c1))
    #c1, c2 = stall(9, 5)
    #print("Case #{}: {} {}".format(1, c2, c1))