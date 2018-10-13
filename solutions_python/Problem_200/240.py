import fileinput


def ascend(n):
    if not n:
        return True
    for left, right in zip(n, n[1:]):
        if left > right:
            return False
    return True


def solve(n):
    if ascend(n):
        return n
    m = str(int(n) - int(n[-1]) - 1)
    return solve(m[:-1]) + "9"


f = fileinput.input()
cases = int(f.readline().strip())
for case in range(cases):
    num = f.readline().rstrip()
    print "Case #{}: {}".format(case + 1, solve(num))
