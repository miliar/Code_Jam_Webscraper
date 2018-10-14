#!/usr/bin/env python
import argparse


def parse_pancake_string(pancake_string):
    pancake_state = []
    for c in pancake_string:
        if c == '+':
            pancake_state.append(True)
        else:
            pancake_state.append(False)
    return pancake_state


def parse_file(filename):
    problems = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                num_problems = int(line)
            else:
                line = line.split(' ')
                assert len(line) == 2
                pancake_state = parse_pancake_string(line[0])
                spatula_length = int(line[1])
                problems.append((pancake_state, spatula_length))

    assert num_problems == len(problems)

    return problems


def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print('Case #{}: '.format(i + 1), end='')
        if solution == -1:
            print('IMPOSSIBLE')
        else:
            print(solution)


def is_solved(state):
    for p in state:
        if not p:
            return False
    return True


def flip_at(index, state, spatula_length):
    new_state = list(state)
    new_state[index:(index + spatula_length)] = [
        not s for s in new_state[index:(index + spatula_length)]
    ]
    return new_state


def solve_problem(problem):
    state, spatula_length = problem
    state = list(state)

    # check if already solved
    if is_solved(state):
        return 0

    if len(state) < spatula_length:
        return -1

    flip_count = 0

    # if there is a minus at either end, flip immediately
    if not state[0]:
        flip_count += 1
        state = flip_at(0, state, spatula_length)
    if not state[-1]:
        flip_count += 1
        state = flip_at(0, state[::-1], spatula_length)[::-1]

    if len(state) - 2 >= spatula_length:
        child_flip_count = solve_problem((state[1:-1], spatula_length))
        if child_flip_count == -1:
            return -1

        flip_count += child_flip_count
    elif not is_solved(state):
        return -1

    return flip_count


def main():
    parser = argparse.ArgumentParser(
        description='Parse problem file output solution')
    parser.add_argument('--input-file')
    parser.add_argument(
        '--state', type=str, default=None, help='Plus/Minus string')
    parser.add_argument(
        '--len', type=int, default=None, help='Length of spatula')

    args = parser.parse_args()

    if args.state is None and args.len is None:
        problems = parse_file(args.input_file)
    else:
        problems = [(parse_pancake_string(args.state), args.len)]
    solutions = [solve_problem(problem) for problem in problems]
    print_solutions(solutions)


if __name__ == '__main__':
    main()
