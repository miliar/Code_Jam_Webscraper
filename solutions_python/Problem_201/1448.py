# 2017 Google Code Jam, Charlie Crandall
def stall_finder(n, k):
    ls = int((n - 1) / 2)
    rs = int(n - int((n - 1)/ 2) - 1)
    if k == 1:
        return (ls, rs)
    else:
        if k % 2 == 0:
            next_level = stall_finder(rs, k / 2)
        else:
            next_level = stall_finder(ls, (k - 1) / 2)
        return next_level


with open('C-small-2.in') as f:
    for i, line in enumerate(f.readlines()[1:], start=1):
        n, k = [int(x) for x in line.split()]
        ls, rs = stall_finder(n, k)

        output = '{} {}'.format(max(ls, rs), min(ls, rs))
        print("Case #{}: {}".format(str(i), output))
