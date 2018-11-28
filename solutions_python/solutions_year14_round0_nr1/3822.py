import sys

def main(filename):
    # print filename
    with open(filename) as f:
        lines = f.readlines()
        num_cases = int(lines[0])
        cases = lines[1:]
        # print cases
        start = 0
        for i in range (0, num_cases):
            first_choice = get_row(cases[start:start+5])
            start += 5
            second_choice = get_row(cases[start:start+5])
            start += 5
            judge_trick(i, first_choice, second_choice)

def judge_trick(case, first_choice, second_choice):
    result = "Case #%d: " % (case + 1)
    first = set(first_choice)
    second = set(second_choice)
    magic_result = first & second
    if len(magic_result) == 1:
        result += magic_result.pop()
    elif len(magic_result) > 1:
        result += 'Bad magician!'
    else:
        result += 'Volunteer cheated!'
    print result


def get_row(case):
    selected = int(case[0]) - 1
    grid = []
    for row in case[1:]:
        grid.append(row.split())
    return grid[selected]


if __name__ == "__main__":
    main(sys.argv[1])