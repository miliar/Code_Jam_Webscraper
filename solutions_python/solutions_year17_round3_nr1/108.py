import sys
import math


def solve_case(k, cakes, case_number):
    cakes.sort(key=lambda x: x[1] + x[2])
    cakes.reverse()
    biggest = cakes.pop(0)
    area = biggest[1] + biggest[2]
    current_biggest = biggest
    for _ in range(1, k):
        for idx, cake in enumerate(cakes):
            d = (cake[0] * cake[0] * math.pi) - (current_biggest[0] * current_biggest[0] * math.pi)
            if d > 0:
                cakes[idx] = (cake[0], d, cake[2])
            else:
                cakes[idx] = (cake[0], 0, cake[2])
        cakes.sort(key=lambda x: x[1] + x[2])
        cakes.reverse()
        biggest = cakes.pop(0)
        area += (biggest[1] + biggest[2])
        if biggest[0] > current_biggest[0]:
            current_biggest = biggest

    print("Case #%d: %f" % (case_number, area))


def main():
    f = sys.stdin
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')

    total_cases = f.readline()
    for case_number in range(1, int(total_cases) + 1):
        n, k = map(int, f.readline().strip().split(' '))
        cakes = []
        for _ in range(0, n):
            r, h = map(int, f.readline().strip().split(' '))
            cakes.append((r, r * r * math.pi, r * 2 * math.pi * h))

        solve_case(k, cakes, case_number)

if __name__ == "__main__":
    main()
