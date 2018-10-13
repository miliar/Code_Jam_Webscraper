import fileinput

CPS = 2.0


def fastest(c, f, x):
    t = 0
    cps = CPS
    best_solution_found = None

    while True:
        time_to_win = x / cps
        time_to_buy_farm = c / cps

        if not best_solution_found:
            best_solution_found = t + time_to_win

        if t + time_to_buy_farm >= best_solution_found:
            # We already found a solution that beats creating another farm
            return best_solution_found

        # Let's record the best solution found...
        best_solution_found = min(best_solution_found, t + time_to_win)

        # ...and create another farm
        cps += f
        t += time_to_buy_farm


def main(files=None):
    ff = fileinput.input(files)
    readline = lambda: ff.readline().strip()

    total = int(readline())
    for i in xrange(total):
        c, f, x = map(float, readline().split())
        print "Case #{}: {:.7f}".format(
            i + 1,
            fastest(c, f, x)
        )


main()
