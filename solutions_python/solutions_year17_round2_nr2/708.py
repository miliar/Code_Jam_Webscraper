import fileinput
import math


INPUT = "B-small.in"
OUTPUT = "B-small.out"

DEBUG = True


def solve(problem):
    n, *_ = problem
    n = int(n)
    unicorns = {'R': int(problem[1]),
                'Y': int(problem[3]),
                'B': int(problem[5]),
                'G': int(problem[4]),
                'O': int(problem[2]),
                'V': int(problem[6])}
    stalls = []
    cid = 0
    previous = ''
    first = max(unicorns, key=unicorns.get)
    color = first
    while True:
        if color != previous and unicorns[color] > 0:
            if unicorns[first] == unicorns[color] and first != previous:
                color = first
            stalls.append(color)
            previous = color
            unicorns[color] -= 1
            n -= 1
            color = max(unicorns, key=unicorns.get)
        else:
            mem_color = color
            mem_value = unicorns[color]
            unicorns[mem_color] = -1
            color = max(unicorns, key=unicorns.get)
            if unicorns[first] == unicorns[color]:
                color = first
            unicorns[mem_color] = mem_value

        if n == 0:
            return stalls if stalls_valid(stalls) else ["IMPOSSIBLE"]
        if  unicorns[color] > 1 and unicorns[color] == n:
            return "IMPOSSIBLE"


def put_unicorn(unicorns, stalls, color):
    stalls.append(color)
    unicorns[color] -= 1


def stalls_valid(stalls):
    left = stalls[0]
    for s in stalls[1:]:
        if s == left:
            return False
        left = s
    return stalls[0] != stalls[-1]



def format_solution(solution):
    return ''.join(solution)


def main():
    output_lines = []

    with fileinput.input(INPUT) as f:
        for case in range(1, int(f.readline())+1):
            problem = f.readline().split()

            if DEBUG:
                debug(*problem)

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
