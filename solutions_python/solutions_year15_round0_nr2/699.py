import sys

def optimal_time(pancakes, level):
    pancakes.sort(reverse=True)
    highest_stack = pancakes[0]
    rest = pancakes[1:]
    if level < 9:
        solutions = [highest_stack]
        half_stack = int(highest_stack/2)
        for i in range(1, half_stack + 1):
            solutions.append(optimal_time(rest + [highest_stack - i, i], level + 1) + 1)
        solutions.sort()
        return solutions[0]
    else:
        return highest_stack

def run_test(case_number, generator):
    ignore = next(generator)
    optimal = -1
    pancakes = [int(x) for x in next(generator).split()]
    print('Case #%d: %d' % (case_number, optimal_time(pancakes, 0)))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()