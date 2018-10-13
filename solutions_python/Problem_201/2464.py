import sys


def run_stalls(n_stalls, n_people):
    # type: (int, int) -> str
    res = ''
    stalls_free = [n_stalls]
    left = 0
    right = 0
    should_print = n_stalls < 50

    if should_print:
        print "%d %d" % (n_stalls, n_people)
        print "O " + ". " * n_stalls + "O"

    for person in range(n_people):
        empty_max = max(stalls_free)
        stall_idxs = []
        for idx, stall in enumerate(stalls_free):
            if stall == empty_max:
                stall_idxs.append(idx)

        stall = stall_idxs[0]
        free = stalls_free[stall]
        right = free / 2
        left = (free - right) - 1
        stalls_free[stall] = left
        stalls_free.insert(stall + 1, right)

    if should_print:
        print stalls_free
        print "O",
        for idx, free in enumerate(stalls_free, 1):
            for x in range(free):
                print ".",
            if idx != len(stalls_free):
                print "O",
        print "O"
        print right
        print left

    res = "%d %d" % (right, left)

    return res


def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()

    t = int(lines.pop(0))
    assert t == len(lines)

    results = []
    for idx, case in enumerate(lines, 1):
        n, k = map(int, case.split())

        if n == k:
            result = "0 0"
        else:
            result = run_stalls(n, k)
        case_str = "Case #%d: %s" % (idx, result)
        print case_str
        results.append(case_str + '\n')

    with open(sys.argv[1] + ".out", "w") as fp:
        fp.writelines(results)


if __name__ == "__main__":
    main()
