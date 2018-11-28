import sys

__author__ = 'Saran'


class FoundWinner(Exception):
    pass


def check_xo(count_case, xo):
    count_dot = 0

    #Check Horizontal
    for x in range(0, 4):
        if (xo[x].count('X') + xo[x].count('T')) == 4:
            msg = 'Case #' + str(count_case + 1) + ': X won'
            return msg
        if (xo[x].count('O') + xo[x].count('T')) == 4:
            msg = 'Case #' + str(count_case + 1) + ': O won'
            return msg
        count_dot += xo[x].count('.')

    #Check Vertical
    for y in range(0, 4):
        check_list = (xo[0][y], xo[1][y], xo[2][y], xo[3][y])
        if (check_list.count('X') + check_list.count('T')) == 4:
            msg = 'Case #' + str(count_case + 1) + ': X won'
            return msg
        if (check_list.count('O') + check_list.count('T')) == 4:
            msg = 'Case #' + str(count_case + 1) + ': O won'
            return msg
        count_dot += check_list.count('.')

    #Check Diagonal
    check_list = (xo[0][0], xo[1][1], xo[2][2], xo[3][3])
    if (check_list.count('X') + check_list.count('T')) == 4:
        msg = 'Case #' + str(count_case + 1) + ': X won'
        return msg
    if (check_list.count('O') + check_list.count('T')) == 4:
        msg = 'Case #' + str(count_case + 1) + ': O won'
        return msg
    check_list = (xo[0][3], xo[1][2], xo[2][1], xo[3][0])
    if (check_list.count('X') + check_list.count('T')) == 4:
        msg = 'Case #' + str(count_case + 1) + ': X won'
        return msg
    if (check_list.count('O') + check_list.count('T')) == 4:
        msg = 'Case #' + str(count_case + 1) + ': O won'
        return msg

    if count_dot == 0:
        msg = 'Case #' + str(count_case + 1) + ': Draw'
    else:
        msg = 'Case #' + str(count_case + 1) + ': Game has not completed'
    return msg


def main(input_file, output_file):
    file_input = open(input_file)
    file_output = open(output_file, "w")
    case = int(file_input.readline())
    for count_case in range(0, case):
        #Create XO List of this case
        xo = list()
        for count_line in range(0, 4):
            xo.append(list(file_input.readline()[:-1]))
        file_input.readline()

        #Check XO
        print 'Check Case #' + str(count_case + 1) + '... \t',
        output = check_xo(count_case, xo)

        #Write Output to file
        print 'Success | ', output
        file_output.write(output)
        if count_case < case - 1:
            file_output.write('\n')


if __name__ == '__main__':
    '''
    Pass 2 argrument,
    #1 - input file name
    #1 - output file name
    '''
    main(sys.argv[1], sys.argv[2])
