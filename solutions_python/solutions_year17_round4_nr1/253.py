def fu(nstr):
    lowest = int(nstr[len(nstr) - 1])
    for a in range(len(nstr) - 2, -1, -1):
        da = int(nstr[a])
        if da > lowest:
            nstr = nstr[:a] + str(da - 1) + '9' * (len(nstr) - a - 1)
            lowest = da - 1
        else:
            lowest = da
    return str(int(nstr))


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, p = [int(x) for x in input().split()]
    g = [int(x) for x in input().split()]

    ps = [0] * p
    for gi in g:
        ps[gi % p] += 1

    # perfect += ps[0]
#
    # for i2 in range(1, p):
    #     while ps[i2] > 0 and ps[p - i2] > 0:
    #         perfect++
    #         ps[i2]--
    #         ps[p - i2]--

    perfect = 0
    stride = 0
    for i2 in range(0, p):
        while ps[i2] > 0:
            if stride == 0:
                perfect += 1
            ps[i2] -= 1
            stride = (stride + i2) % p

            if stride != 0:
                if ps[p - stride] != 0:
                    ps[p - stride] -= 1
                    stride = 0



    print("Case #{}: {}".format(i, perfect))
