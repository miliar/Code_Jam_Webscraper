def readline_int(f):
    line = f.readline().strip()
    numbers = [int(x) for x in line.split()]
    return numbers if len(numbers) > 1 else numbers[0]

def solve(input_filename):
    input = open(input_filename)
    output = open(output_filename, 'w')

    T = readline_int(input)
    for n in range(T):
        answer_1 = readline_int(input)
        arrangement_1 = [
            readline_int(input)
            for _ in range(4)
        ]
        answer_2 = readline_int(input)
        arrangement_2 = [
            readline_int(input)
            for _ in range(4)
        ]
        result = _solve(
            answer_1,
            arrangement_1,
            answer_2,
            arrangement_2,
        )
        output.write('Case #%d: %s\n' % (n + 1, str(result)))

    input.close()
    output.close()


def _solve(row_1, matrix_1, row_2, matrix_2):
    intersection = set(matrix_1[row_1 - 1]) & set(matrix_2[row_2 - 1])
    l = len(intersection)
    if l == 0:
        return 'Volunteer cheated!'
    if l == 1:
        return list(intersection)[0]
    if l > 1:
        return 'Bad magician!'

solve('A-small-attempt0.in', 'sol.txt')
