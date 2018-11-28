def get_lines(matrix):
    lines = []
    for horizontal in matrix:
        lines.append(horizontal)
    for i in range(0, 4):
        vertical = matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i]
        lines.append(vertical)
    diagonal = ''
    for i in range(0, 4):
        diagonal += matrix[i][i]
    lines.append(diagonal)
    diagonal = ''
    for i in range(0, 4):
        diagonal += matrix[i][3-i]
    lines.append(diagonal)
    return lines


def get_line_result(line):
    x = 0
    o = 0
    has_empty = False
    for char in line:
        if char == 'X':
            x += 1
        elif char == 'O':
            o += 1
        elif char == 'T':
            o += 1
            x += 1
        elif char == '.':
            has_empty = True
    return x, o, has_empty


def process_case(input_lines):
    answers = ["X won", "O won", "Draw", "Game has not completed"]
    answer = None
    matrix = [ input_line for input_line in input_lines.splitlines()]
    for line in get_lines(matrix):
        x, o, has_empty = get_line_result(line)
        if x == 4:
            answer = answers[0]
        elif o == 4:
            answer = answers[1]
    if not answer:
        if not has_empty:
            answer = answers[2]
        else:
            answer = answers[3]
    return answer


def read_input():
    input_lines = ''
    input_line = raw_input()
    while(input_line):
        input_lines += input_line + '\n'
        input_line = raw_input()
    return input_lines


def process_input():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases + 1):
        input_lines = read_input()
        answer = process_case(input_lines)
        print 'Case #%d: %s' % (case_number, answer)


if __name__ == '__main__':
    process_input()
