def solve2(a):
    p = None
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            p = i
            break

    if p is None:
        return "".join([str(d) for d in a])

    a[p] = a[p] - 1
    for i in range(p + 1, len(a)):
        a[i] = 9

    if a[0] == 0:
        a.pop(0)

    return solve2(a)


def solve():
    return solve2([int(c) for c in input()])


def prepare_input():
    local = False
    task = 'B'
    attempt = -1

    import sys

    if local:
        sys.stdin = open("../input.txt", "r")
    else:
        filename = "../{}-small-attempt{}".format(task, attempt) if attempt >= 0 else "../{}-large".format(task)

        sys.stdin = open(filename + ".in", "r")
        sys.stdout = open(filename + ".out", "w")

        print("filename:", filename[3:], file=sys.stderr)


prepare_input()
tests = int(input())
for test in range(1, tests + 1):
    res = solve()
    print("Case #{}: {}".format(test, res))
