import sys

def main():
    lines = sys.stdin.readlines()
    problems = parse_problems(lines)
    solutions = [solve(problem) for problem in problems]
    print_solutions(solutions)

def parse_problem(itr):
    nep = int(next(itr).strip())
    pancakes = [int(p.strip()) for p in next(itr).split()]
    assert len(pancakes) == nep
    return pancakes

def solve(problem):
    _, basic_celing = basic_plan(problem[:])

    best = None
    best_celing = None

    for celing in range(basic_celing, 0, -1):
        splits = cap_height(problem, celing)
        time = splits + celing
        if best is None or time <= best:
            best = time
            best_celing = celing
        else:
            break

    return best

def cap_height(stacks, celing):
    # If no splits time is equal to the highest stack
    stacks = [stack for stack in stacks if stack > celing]
    specials = 0
    while True:
        changed = False
        for i, height in enumerate(stacks):
            if height > celing:
                stacks[i] -= celing
                specials += 1
                changed = True
        if not changed:
            break
    return specials


def basic_plan(problem):
    stacks = problem

    # If no splits time is equal to the highest stack
    tallest = max(stacks)
    if tallest <= 3:
        return 0, tallest

    # Split the largest stack
    tallest_index = stacks.index(tallest)
    stacks[tallest_index] -= tallest / 2
    stacks.append(tallest / 2)

    # Recursive calculation
    sub_split_time, sub_wait_time = basic_plan(stacks)
    sub_time = sub_split_time + sub_wait_time
    if tallest <= sub_time:
        return 0, tallest
    else:
        return sub_split_time + 1, sub_wait_time

def verify(stacks, split, verbose=False):
    stacks = stacks[:]
    stacks.sort(reverse=True)
    time = 0

    if verbose:
        print('=' * 60)
        print('Stacks: {}'.format(stacks))
        print('Split: {}'.format(split))
        print('-' * 60)
        print('{} {} {}'.format(time, 'start', stacks))

    # Split
    for i in range(split):
        max_height = stacks[0]
        stacks[0] = max_height / 2
        stacks.append(max_height - stacks[0])
        stacks.sort(reverse=True)
        time += 1
        if verbose:
            print('{} {} {}'.format(time, 'split', stacks))

    # Wait
    while any(stacks):
        stacks = [max(0, stack - 1) for stack in stacks]
        time += 1
        if verbose:
            print('{} {} {}'.format(time, 'wait ', stacks))

    if verbose:
        print('-' * 60)
    return time


def print_solutions(solutions):
    for index, solution in enumerate(solutions):
        print('Case #{}: {}'.format(index + 1, solution))

def parse_problems(lines):
    itr = iter(lines)
    count = int(next(itr).strip())
    problems = []
    for i in range(count):
        problems.append(parse_problem(itr))
    assert len(problems) == count
    return problems

if __name__ == '__main__':
    main()
