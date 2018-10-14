import fileinput


INPUT = "A-large.in"
OUTPUT = "A-large.out"

DEBUG = True


def solve(problem):
    d, n, horses = problem
    max_ti = 0
    for ki, si in horses:
        max_ti = max(max_ti, (d-ki)/si)

    solution = d / max_ti
    return solution


def format_solution(solution):
    return "{0:.6f}".format(solution)


def main():
    output_lines = []

    with fileinput.input(INPUT) as f:
        for case in range(1, int(f.readline())+1):
            d, n = f.readline().split()

            d = int(d)
            n = int(n)
            horses = []
            for i in range(n):
                ki, si = f.readline().split()
                ki = int(ki)
                si = int(si)
                horses.append((ki, si))

            problem = [d, n, horses]
            if DEBUG:
                debug(problem)

            solution = format_solution(solve(problem))

            append_output(case, solution, output_lines)

    write_output(output_lines)


def append_output(case, solution, output_lines):
    out = "Case #{}: {}\n".format(case, solution)
    print("[OUT] " + out)
    output_lines.append(out)


def write_output(output_lines):
    with open(OUTPUT, "w+") as f:
        f.writelines(output_lines)


def debug(*texts):
    print("[DEBUG]", *texts)


if __name__ == "__main__":
    main()
