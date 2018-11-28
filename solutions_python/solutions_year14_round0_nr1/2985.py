import sys

def print_solution(case, message):
    print "Case #%s: %s" % (case, message)

def make_grid(lines):
    return [[int(val) for val in row] for row in lines.split()]

lines = sys.stdin.readlines()
test_cases = int(lines[0])

for case in range(1, test_cases + 1):
    first_row_index = 1 + 10 * (case - 1)
    second_row_index = first_row_index + 5

    first_row_num = int(lines[first_row_index])
    second_row_num = int(lines[second_row_index])
    
    first_row = [int(val) for val in lines[first_row_index + first_row_num].split()]
    second_row = [int(val) for val in lines[second_row_index + second_row_num].split()]
    answer = set(first_row).intersection(set(second_row))

    if len(answer) == 1:
        print_solution(case, answer.pop())
    elif len(answer) == 0:
        print_solution(case, "Volunteer cheated!")
    else:
        print_solution(case, "Bad magician!")
