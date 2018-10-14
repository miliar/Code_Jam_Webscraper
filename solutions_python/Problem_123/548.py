def solve(a, motes):
    if not motes:
        return 0
    m = motes[0]
    if a > m:
        return solve(a + m, motes[1:])
    else:
        if a != 1:
            return min(
                solve(a, motes[1:]) + 1,
                solve(a, [a-1] + motes) + 1
            )
        else:
            return solve(a, motes[1:]) + 1


def main():
    n = int(raw_input())
    for i in range(n):
        a, nbr_m = map(int, raw_input().split())
        motes = map(int, raw_input().split())
        motes.sort()
        res = solve(a, motes)
        print "Case #%d: %d" % (i + 1, res)


if __name__ == '__main__':
    main()
