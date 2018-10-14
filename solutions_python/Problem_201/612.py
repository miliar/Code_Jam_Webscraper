import sys

T = int(sys.stdin.readline())
tests = []
for i in range(T):
    n, k = sys.stdin.readline().split(" ")
    tests.append((int(n), int(k)))


def solve(n, k):
    vals = {}
    big = n
    vals[big] = 1
    i = 0
    while i < k:
        n2 = (big-1)/2
        n1 = big - 1 - n2
        vals.setdefault(n1, 0)
        vals.setdefault(n2, 0)
        vals[n1] += vals[big]
        vals[n2] += vals[big]
        i += (vals[big])
        del vals[big]
        big = max(vals.keys())
    return n1, n2


for nb, t in enumerate(tests):
    res = solve(*t)
    sys.stdout.write("Case #{}: {} {}\n".format(nb+1, res[0], res[1]))
