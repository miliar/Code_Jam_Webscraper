import sys


def problem_instances(filename):
    f = open(filename)
    num_instances = int(f.readline())
    for i in range(num_instances):
        lines = []
        for i in range(4):
            lines.append(f.readline().strip())
        f.readline()
        yield lines

def check_rows(lines):
    for line in lines:
        if "." not in line and "O" not in line:
            return "X won"
        if "." not in line and "X" not in line:
            return "O won"

def check_columns(lines):
    return check_rows(zip(*lines))

def check_diagonals(lines):
    diag1 = [lines[n][n] for n in range(4)]
    diag2 = [lines[n][3-n] for n in range(4)]
    return check_rows((diag1, diag2))

def solve(instance):
    lines = instance
    for func in (check_rows, check_columns, check_diagonals):
        res = func(lines)
        if res:
            return res

    if "." not in "".join(lines):
        return "Draw"
    return "Game has not completed"


filename = sys.argv[1]
out = open(filename + ".out", "w")
for idx, instance in enumerate(problem_instances(filename), 1):
    out.write("Case #%i: %s\n" % (idx, solve(instance)))