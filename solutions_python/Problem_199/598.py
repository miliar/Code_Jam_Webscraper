import sys

T = int(sys.stdin.readline())
tests = []
for i in range(T):
    s, k = sys.stdin.readline().split(" ")
    tests.append((int(k), [1 if c == "+" else 0 for c in s]))


def solve_test(test):
    k, l = test
    n = len(l)
    flips = [0]*n
    tmp = 0  # nb of previous flips impacting the current pancake
    for i in range(k-1, len(flips)):
        # has not been flipped the right number of times
        if (tmp + l[i-k+1]) % 2 == 0:
            tmp += 1
            flips[i] = 1
        tmp -= flips[i-k+1]
    for j in range(n-k+1, n):
        # print "{0}, j: {1} tmp: {2} l[{1}]={3}".format(l, j, tmp, l[j])
        if (tmp + l[j]) % 2 == 0:
            return None
        tmp -= flips[j]
    return sum(flips)


for nb, t in enumerate(tests):
    res = solve_test(t)
    sys.stdout.write("Case #{}: {}\n".format(
        nb+1, res if res is not None else "IMPOSSIBLE"))
