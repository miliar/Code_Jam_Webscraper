def calc_ans(input_file):
    [n, m] = [int(x) for x in input_file.readline().split()]
    table = []
    for x in xrange(n):
        table += [[int(x) for x in input_file.readline().split()]]

    if n == 1 or m == 1:
        return 'YES'

    max_in_line = []
    max_in_column = [1] * m
    for line in table:
        max_in_line += [max(line)]
        for x in xrange(m):
            if line[x] > max_in_column[x]:
                max_in_column[x] = line[x]

    for x in xrange(n):
        for y in xrange(m):
            if table[x][y] < max_in_line[x] and table[x][y] < max_in_column[y]:
                return 'NO'
    return 'YES'


def main():
    filename_input = 'input_b_.in'
    filename_output = 'output_b_large.txt'
    result = []
    with open(filename_input, 'r') as input_file:
        t = int(input_file.readline())
        for testCase in xrange(1, t + 1):
            ans = calc_ans(input_file)
            s = 'Case #' + str(testCase) + ': ' + str(ans) + '\n'
            result += [s]
    with open(filename_output, 'w') as output_file:
        output_file.writelines(result)


main()