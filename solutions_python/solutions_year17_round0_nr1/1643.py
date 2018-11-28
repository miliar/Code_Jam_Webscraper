import sys


def solve(boolean_pancakes, flip_size):
    flips = 0

    i = 0
    while i+flip_size <= len(boolean_pancakes):
        p = boolean_pancakes[i]
        if not p:
            flips += 1
            for j in range(flip_size):
                boolean_pancakes[i+j] = not boolean_pancakes[i+j]

        i += 1

    if not all(boolean_pancakes[(-1 * flip_size):]):
        return "IMPOSSIBLE"
    
    return flips

num_cases = int(sys.stdin.readline())

for case_index in range(num_cases):
    case_line = sys.stdin.readline()
    pancakes, flip_size = case_line.split(' ')
    boolean_pancakes = [x == '+' for x in pancakes]

    answer = solve(boolean_pancakes, int(flip_size))

    print("Case #{}: {}".format(case_index+1, answer))
