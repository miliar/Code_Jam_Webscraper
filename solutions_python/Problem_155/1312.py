from sys import stdin


def readline():
    return stdin.readline().strip()


def solve(levels):
    toinvite = 0
    total = 0
    for i, level in enumerate(levels):
        if i == 0:
            total = level
            continue
        if level == 0:
            continue
        if total >= i:
            total += level
        else:
            toinvite += i - total
            total += i - total + level
    return toinvite


if __name__ == "__main__":
    numofcases = int(readline())
    for i in range(numofcases):
        smax, levels = readline().split(' ')
        smax = int(smax)
        levels = map(int, levels)
        result = solve(levels)
        print 'Case #%d: %d' % (i + 1, result)
