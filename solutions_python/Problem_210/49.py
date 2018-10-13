import sys


def get_exch(fixed):
    """Get the minimum number of exchanges."""

    # Fixed, partially fixed.
    acc = (
        [0, []],
        [0, []]
    )
    even = []

    fixed.sort()
    last = len(fixed) - 1
    for i, v in enumerate(fixed):
        begin, end, who = v
        acc[who][0] += end - begin

        if i == last:
            next_begin = fixed[0][0] + 24 * 60
            next_who = fixed[0][2]
        else:
            next_begin = fixed[i + 1][0]
            next_who = fixed[i + 1][2]

        if next_who == who:
            acc[who][1].append(next_begin - end)
        else:
            even.append(next_begin - end)

    n_exch = len(even)

    TOTAL = 12 * 60
    for i, j in acc:
        curr = i
        j.sort()
        for k, v in enumerate(j):
            if curr + v <= TOTAL:
                curr += v
            else:
                end = k
                break
        else:
            end = len(j)

        n_give_up = len(j) - end
        n_exch += 2 * n_give_up
        continue

    return n_exch


def main():
    """The main driver."""
    inp = open(sys.argv[1], 'r')
    n_tests = int(inp.readline())
    for test_idx in range(n_tests):
        ac, aj = [int(i) for i in inp.readline().split()]
        fixed = []
        for i, v in enumerate([ac, aj]):
            for _ in range(v):
                fixed.append(tuple(
                    int(j) for j in inp.readline().split()
                ) + (i, ))
                continue
            continue
        print('Case #{}: {}'.format(
            test_idx + 1, get_exch(fixed)
        ))
        continue

if __name__ == '__main__':
    main()






