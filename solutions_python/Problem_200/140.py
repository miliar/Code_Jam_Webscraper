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
    nstr = input().strip()  # read a list of integers, 2 in this case
    outs = fu(nstr)
    n = int(nstr)
    out = int(outs)
    # for x in range(out + 1, n + 1):
    #     xstr = str(x)
    #     tidy = True
    #     for (a, b) in zip(xstr, xstr[1:]):
    #         if int(a) > int(b):
    #             tidy = False
    #             break
    #     if tidy:
    #         print('???: {} {} {}'.format(n, out, x))

    print("Case #{}: {}".format(i, outs))
