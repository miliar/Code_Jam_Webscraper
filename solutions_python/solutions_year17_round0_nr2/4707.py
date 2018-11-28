def int_to_list(n):
    return list(map(int, str(n)))


def is_tidy(n):
    n_lst = int_to_list(n)
    max_num = 0
    for i in n_lst:
        if i < max_num:
            return False
        max_num = i
    return True


def get_last_tidy(n):
    while n > 0:
        if is_tidy(n):
            break
        n -= 1
    return n


def last_tidy_to_str(i, n):
    return str.format('Case #%d: %d\n' % (i, get_last_tidy(n)))


file_input_name = 'B-small-attempt0.in'
file_output_name = 'B-small-attempt0.out'

if __name__ == '__main__':
    file_input = open(file_input_name, 'r')
    file_output = open(file_output_name, 'w')

    t = int(file_input.readline())

    for i in range(1, t + 1):
        n = int(file_input.readline()[:-1])
        file_output.write(last_tidy_to_str(i, n))
