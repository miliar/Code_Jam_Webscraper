import sys
import math


# Only for small.
def solve_case(p, gs, case_number):
    rest = [g for g in gs if g % p != 0]
    fg = len(gs) - len(rest)
    mods = [g % p for g in rest]
    g1 = mods.count(1)
    g2 = mods.count(2)
    if g1 > g2:
        fg += g2
        fg += int(math.ceil(float((g1 - g2)) / p))
    else:
        fg += g1
        fg += int(math.ceil(float((g2 - g1)) / p))
    print("Case #%d: %d" % (case_number, fg))


def main():
    r = sys.stdin
    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        p = int(r.readline().strip().split(' ')[1])
        gs = list(map(int, r.readline().strip().split(' ')))

        solve_case(p, gs, case_number)

if __name__ == "__main__":
    main()
