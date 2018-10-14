
def main():
    filename = 'A-small-attempt1.in'
    magic_trick(filename)


def magic_trick(infilename):
    f = open(infilename, 'r')

    num_tests = int(f.readline())

    for i in range(0, num_tests):
        row1 = read_row_choice(f)
        array1 = read_array(f, 4)
        row2 = read_row_choice(f)
        array2 = read_array(f, 4)
        possible_numbers = report_matches(array1[row1], array2[row2])
        print_output(possible_numbers, i)


def report_matches(row1, row2):
    temp = row1
    temp.extend(row2)
    return list(set([x for x in temp if temp.count(x) > 1]))


def read_row_choice(fileobj):
    return(int(fileobj.readline()) - 1)


def read_array(fileobj, arrsize):
    arr = []
    for i in range(0, arrsize):
        arr.append(_read_array_line(fileobj))
    return arr


def _read_array_line(fileobj):
    return [int(a) for a in fileobj.readline().split(' ')]


def print_output(possible_numbers, i):
    n_matches = len(possible_numbers)
    i = i + 1

    if n_matches == 1:
        print('Case #{case}: {number}'.format(number=int(possible_numbers[0]),
                                              case=i))

    elif n_matches > 1:
        print('Case #{case}: Bad magician!'.format(case=i))

    elif n_matches < 1:
        print('Case #{case}: Volunteer cheated!'.format(case=i))

    else:
        print('Whaaat....?')


if __name__ == '__main__':
    main()

