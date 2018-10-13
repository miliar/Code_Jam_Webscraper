def pancake_flipper(pancakes, n):
    # setup - creating binary representation of problem string, masks, and goal
    pancakes = pancakes.replace('+','1')
    pancakes = pancakes.replace('-','0')
    griddle_size = len(pancakes)
    goal = int('1' * griddle_size,2)
    masks = []

    for i in range(griddle_size - (n-1)):
        masks.append(int('0'*i + '1'*n + '0'*(griddle_size-n-i),2))
    pancakes = int(pancakes,2)


    # begin actual search algorithm
    griddle_states = set()
    griddle_states.add(pancakes)
    progress = True
    steps = 0
    if pancakes == goal:
        goal_found = True
    else:
        goal_found = False

    while progress and not goal_found:
        progress = False
        num_states = len(griddle_states)
        for state in frozenset(griddle_states):
            for mask in masks:
                griddle_states.add(state ^ mask)
        if len(griddle_states) > num_states:
            progress = True
        if goal in griddle_states:
            goal_found = True
        steps += 1

    if goal_found:
        return steps
    else:
        return 'IMPOSSIBLE'

def solve_file(file_path):
    f = open(file_path)
    solution = open('results.txt','w')
    # skip first line and read remaining lines
    case_number = 1
    for line in f.readlines()[1:]:
        parsed_line = line.split()
        result = pancake_flipper(parsed_line[0],int(parsed_line[1]))
        print('Case #{}: {}'.format(case_number,result),file=solution)
        case_number += 1


solve_file('A-small-attempt0.in')
