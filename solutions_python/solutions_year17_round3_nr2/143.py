def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        nc, nj = [int(s) for s in raw_input().split(" ")]
        ac = [[int(s) for s in raw_input().split(" ")] for _ in range(nc)]
        aj = [[int(s) for s in raw_input().split(" ")] for _ in range(nj)]

        print "Case #{}: {}".format(i, solve(nc, nj, ac, aj))


def solve(nc, nj, ac, aj):
    if nc + nj == 1:
        return 2

    ac.sort()
    aj.sort()

    if nc == 0:
        x = aj[1][1] - aj[0][0]
        y = aj[0][1] + 1440 - aj[1][0]
        return 2 if (x <= 720 or y <= 720) else 4

    if nj == 0:
        x = ac[1][1] - ac[0][0]
        y = ac[0][1] + 1440 - ac[1][0]
        return 2 if (x <= 720 or y <= 720) else 4

    return 2


if __name__ == '__main__':
    main()
