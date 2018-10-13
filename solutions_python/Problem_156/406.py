from math import ceil


def solve_problem(file_name):
    input_file = file_name + ".in"
    output_file = file_name + ".out"
    f = open(input_file, "r")
    g = open(output_file, "w")

    # Get test cases:
    
    test_cases = int(f.readline())
    for test_case in range(1, test_cases + 1):
        length = f.readline()
        pancakes = map(int, f.readline().split())
        answer = solve_test_case(pancakes)
        result = "Case #" + str(test_case) + ": " + str(answer) + "\n"
        g.write(result)
        print result

    return "Done"

def solve_test_case(pancakes):

    # Try every scenario where we set:
    # how many pancakes one person can eat.
    upper_bound = max(pancakes) # should be no more than what's given

    best_time = float("inf")
    for max_pancakes in range(upper_bound, 0, -1):
        moves_required = 0
        for pancake_stack in pancakes:
            moves_required += moves_needed(pancake_stack, max_pancakes)
        time = max_pancakes + moves_required
        best_time = min(best_time, time)
    return best_time

def moves_needed(pancakes, max_pancakes):
    pancakes = float(pancakes)
    max_pancakes = float(max_pancakes)
    moves_needed = ceil(pancakes / max_pancakes)
    return int(moves_needed) - 1

print solve_problem("B-large")
