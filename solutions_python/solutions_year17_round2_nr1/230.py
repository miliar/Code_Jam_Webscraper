def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        d, n = [int(s) for s in raw_input().split(" ")]
        horses = [[int(s) for s in raw_input().split(" ")] for _ in range(n)]

        print "Case #{}: {}".format(i, solve(horses, d, n))


def solve(horses, d, n):
    min_time = max((d - horse[0]) * 1. / horse[1] for horse in horses)

    return d / min_time


if __name__ == '__main__':
    main()
