
def get_common(row1, matrix1, row2, matrix2):
    items1 = set(matrix1[row1 - 1])
    items2 = set(matrix2[row2 - 1])
    return items1 & items2


def get_msg(myset):
    if len(myset) == 1:
        msg = '%d' % list(myset)[0]
        return msg
    elif len(myset) == 0:
        msg = 'Volunteer cheated!'
        return msg
    elif len(myset) > 1:
        msg = 'Bad magician!'
        return msg


def write_to_file(output_path, content):
    with open(output_path, 'w+') as output_file:
        output_file.write(content)


if __name__ == '__main__':
    input_path = 'A-small-attempt0.in'
    output_path = 'A-small-attempt0.out'
    outputlines = []
    with open(input_path) as input_file:
        T = int(input_file.readline())
        # print T
        for case in range(T):
            row1 = int(input_file.readline())
            matrix1 = []
            for _ in range(4):
                matrix1.append([int(x) for x in input_file.readline().split()])

            row2 = int(input_file.readline())
            matrix2 = []
            for _ in range(4):
                matrix2.append([int(x) for x in input_file.readline().split()])
            # print matrix1
            # print matrix2
            myset = get_common(row1, matrix1, row2, matrix2)
            msg = get_msg(myset)
            outputlines.append('Case #%d: %s' % (case + 1, msg))
        write_to_file(output_path, '\n'.join(outputlines))
        print outputlines

