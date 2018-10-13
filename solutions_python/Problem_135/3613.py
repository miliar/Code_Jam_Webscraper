import sys

lines = [line.strip() for line in sys.stdin.readlines()]
test_cases = int(lines.pop(0))

def read_answer():
    answer = int(lines.pop(0))
    grid = []
    for _ in range(4):
        line = lines.pop(0)
        grid.append([int(n) for n in line.split()])
    return answer, grid

def analyze():
    first_row, first_grid = read_answer()
    second_row, second_grid = read_answer()

    first_options = first_grid[first_row - 1]
    second_options = second_grid[second_row - 1]

    return [x for x in first_options if x in second_options]

for test_case in range(test_cases):
    result = analyze()
    if len(result) == 1:
        output = result[0]
    elif len(result) == 0:
        output = 'Volunteer cheated!'
    else:
        output = 'Bad magician!'
    print 'Case #%s: %s' % (test_case + 1, output)
