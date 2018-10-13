import sys

def main():
    lines = sys.stdin.readlines()
    problems = parse_problems(lines)
    solutions = [solve(problem) for problem in problems]
    print_solutions(solutions)

def solve(problem):
    required = 0
    clapping = 0
    for shyness, count in enumerate(problem):
        missing = shyness - clapping
        required = max(required, missing)
        clapping += count
    return required

def print_solutions(solutions):
    for index, solution in enumerate(solutions):
        print('Case #{}: {}'.format(index + 1, solution))

def parse_problems(lines):
    itr = iter(lines)
    count = int(next(itr).strip())
    for i in range(count):
        top, ratings = next(itr).strip().split()
        assert len(ratings) == int(top) + 1
        yield [int(c) for c in ratings]

if __name__ == '__main__':
    main()
