import sys


def solve(C, F, X):
    solution = X / 2.
    best_solution = solution
    time = 0

    farms = 1
    while True:
        rate = 2
        time = 0
        for i in range(farms):
            time += C / rate
            rate += F

        solution = time + (X / rate)

        if best_solution < solution:
            break
        else:
            best_solution = solution

        farms += 1

    return best_solution



f = sys.stdin

tests = int(f.readline())

for i in range(1,tests+1):
    C,F,X = map(float, f.readline().split())

    print "Case #%d:" % i, round(solve(C, F, X), 7)



