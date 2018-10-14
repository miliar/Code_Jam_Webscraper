def to_int(x):
    return int(x)

def read_problem():
    cases = []
    with open('A-large.in') as f:
        t = int(f.readline())
        for i in range(t):
            cases.append(map(to_int, list(f.readline().split(' ')[1].strip())))
    return cases

def solve_case(case):
    shy_level = 0
    assistants_so_far = 0
    solution = 0
    for assistants in case:
        # print('shy: ' + str(shy_level) + ' - solution: ' + str(solution) + ' - assistants so far: ' + str(assistants_so_far))
        if assistants > 0:
            new_assistants = max(shy_level - assistants_so_far, 0)
            solution += new_assistants
            assistants_so_far += new_assistants
        assistants_so_far += assistants
        shy_level += 1
    return solution

def main():
    cases = read_problem()
    i = 1
    for case in cases:
        solution = solve_case(case)
        print('Case #' + str(i) + ': ' + str(solution))
        i += 1

main()
