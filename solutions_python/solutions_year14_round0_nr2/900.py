def main():
    t = int(raw_input())
    for i in range(1, t + 1):
        res = test()
        print "Case #%d: %.8f" % (i, res)


def test():
    global c, f, x, mem
    [c, f, x] = [float(x) for x in raw_input().split()]

    mem = {0: float(0)}

    i = 0
    while solve(i) > solve(i + 1):
        i += 1
    return solve(i)


def solve(n):
    if n == 0:
        return float((x / (2 + n * f)))
    mem[n] = float(mem[n - 1] + (c / (2 + (n - 1) * f)))
    return float(mem[n] + (x / (2 + n * f)))


main()