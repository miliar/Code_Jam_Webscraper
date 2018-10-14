def process(file_name):
    with open(file_name) as f:
        input = f.readlines()[1:]
    for i, line in enumerate(input):
        ans = get_tidy_number(int(line))
        print 'Case #%s: %s' % (i + 1, ans)


def get_tidy_number(value):
    if value < 10:
        return value

    value_list = int_to_list(value)

    while find_first_smaller_target(value_list) != -1:
        index = find_first_smaller_target(value_list)
        value_list[index - 1] -= 1
        value_list[index:] = [9 for i in value_list[index:]]

    return list_to_int(value_list)


def find_first_smaller_target(value_list):
    for i in range(len(value_list) - 1):
        if value_list[i] > value_list[i + 1]:
            return i + 1
    return -1


def int_to_list(value):
    return [int(d) for d in str(value)]


def list_to_int(value_list):
    res = 0
    for value in value_list:
        res = res * 10 + value
    return res


if __name__ == '__main__':
    process('tidy_number_test_input.txt')
