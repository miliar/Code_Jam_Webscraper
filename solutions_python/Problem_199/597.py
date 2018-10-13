import fileinput

# Solve problem


def flip_pancakes(pancakes, i, k):
    for j in range(i, i + k):
        pancakes[j] = "-" if pancakes[j] is "+" else "+"


def solve_problem(pancakes, k):
    flip_number = 0
    for i in range(len(pancakes) + 1 - k):
        if pancakes[i] is "-":
            flip_number += 1
            flip_pancakes(pancakes, i, k)

    return flip_number if all(pancake is "+" for pancake in pancakes) else "IMPOSSIBLE"

# Utils


def parse_problem(case):
    [pancakes, k] = case.split(" ")
    return list(pancakes), int(k)


def solve_case(case):
    pancakes, K = parse_problem(case)
    solution = solve_problem(pancakes, K)
    print("Case #" + str(index) + ": " + str(solution))


# Main script


for index, line in enumerate(fileinput.input()):
    if index is 0:
        continue

    line = line.strip()
    solve_case(line)
