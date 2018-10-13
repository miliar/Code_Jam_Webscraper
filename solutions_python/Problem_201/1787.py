import fileinput


def compute_left(s):
    ls = [-1]*len(s)
    for i in range(1,len(s)-1):
        if s[i] is not 1:
            ls[i] = ls[i-1] + 1

    return ls


def compute_right(s):
    rs = [-1]*len(s)
    for i in range(len(s)-1, 0, -1):
        if s[i] is not 1:
            rs[i] = rs[i+1] + 1

    return rs


def compute_min(ls, rs):
    m = [-1]*len(ls)
    for i in range(0, len(m)):
        if ls[i] is not -1:
            m[i] = min(ls[i], rs[i])

    return m


def compute_max(ls,rs):
    m = [-1]*len(ls)
    for i in range(0, len(m)):
        if ls[i] is not -1:
            m[i] = max(ls[i], rs[i])

    return m


def solve(n, k):
    # init stools vector
    n = n + 2
    s = [0] * n
    s[0] = 1
    s[n-1] = 1
    small = -1
    large = -1

    for i in range(0, k):
        ls = compute_left(s)
        rs = compute_right(s)
        mini = compute_min(ls, rs)
        maxi = compute_max(ls, rs)
        small = max(mini)
        toplist = list()
        index = list()

        for e in enumerate(mini):
            if e[1] == small:
                index.append(e[0])
                toplist.append(maxi[e[0]])

        large = max(toplist)
        s[index[toplist.index(large)]] = 1

    return large, small

reader = fileinput.input()
t = int(reader.readline())
for i in range(1, t+1):
    n, k = [int(r) for r in reader.readline().split(" ")]
    large, small = solve(n, k)
    print("Case #{}: {} {}".format(i, large, small))


