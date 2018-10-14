# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer


def func(min_1, max_1):
    max_min = []
    m = max(min_)
    for elem in range(0, len(min_1)):
        if min_1[elem] == m:
            max_min.append(elem)

    if len(max_min) == 1:
        return max_min[0]
    else:
        max_max = []
        m = -1
        for a in max_min:
            if max_1[a] > m:
                m = max_1[a]
        for a in max_min:
            if max_1[a] == m:
                max_max.append(a)
        return max_max[0]


for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    l = list()
    l.append(1)
    for r in range(1, n+1):
        l.append(0)

    l.append(1)
    for j in range(0, k):
        min_ = []
        max_ = []
        l_r = []
        for s in range(0, len(l)):
            if l[s] == 0:
                index = s - 1
                n_zero_l = 0
                while l[index] == 0:
                    n_zero_l += 1
                    index -= 1

                index = s + 1
                n_zero_r = 0
                while l[index] == 0:
                    n_zero_r += 1
                    index += 1
                l_r.append((n_zero_l, n_zero_r))
                min_.append(min(n_zero_l, n_zero_r))
                max_.append(max(n_zero_l, n_zero_r))
        index = func(min_1=min_, max_1=max_)
        numero = -1
        for s in range(0, len(l)):
            if l[s] == 0:
                numero += 1
            if numero == index:
                l[s] = 1
    print("Case #{}: {} {}".format(i, max(l_r[index]), min((l_r[index]))))
    # check out .format's specification for more formatting options