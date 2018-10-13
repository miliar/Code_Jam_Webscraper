import math


def get_stall(arg):
    l = []
    arg.sort()
    for p1, p2 in zip(arg, arg[1:]):
        diff = abs(p1 - p2)
        if not l:
            l.append(diff)
            l.append(p1+(diff//2))
            l.append(p1)
        elif l[0] < diff:
            l.clear()
            l.append(diff)
            l.append(p1 + (diff//2))
            l.append(p1)
        else:
            pass
    return l


t = int(input())  # read a line with a single integer
for x in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    if n == k:
        print("Case #{}: {} {}".format(x, 0, 0))
    else:
        ls = [0, n+1]
        blank_list = []
        for i in range(k):
            mee = get_stall(ls)
            # print(mee)
            ls.append(mee[1])
            ls.sort()
            # print("***", ls)
            stall = ls.index(mee[1])
            val1 = ls[stall-1]
            val2 = ls[stall+1]
            z = mee[1]-val1 - 1
            y = val2 - mee[1] - 1
            # y = max(([abs(t - s)//2 for s, t in zip(ls, ls[1:])]))
            # z = min(([abs(t - s)//2 for s, t in zip(ls, ls[1:])]))
            # print("Case #{}: {} {}".format(x, max(abs(mee[1]-mee[0])-1, y), max(abs(mee[2]-mee[1]), abs(z))-1))
        print("Case #{}: {} {}".format(x, max(y, z), min(y, z)))
