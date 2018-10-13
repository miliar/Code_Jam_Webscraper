def get_l_r(n):
    n -= 1
    r = n // 2
    return n - r, r


def find_max_index(n_lst):
    mx = max(n_lst)
    for i in range(len(n_lst)):
        if mx == n_lst[i]:
            return i
    return -1


def new_lst(n_lst):
    index = find_max_index(n_lst)
    temp_l, temp_r = get_l_r(n_lst[index])
    return n_lst[0:index] + list(get_l_r(n_lst[index])) + n_lst[index + 1:], temp_l, temp_r


def find_l_r_for_last_iter(n, k):
    n_lst = [n]
    for i in range(k):
        n_lst, l, r = new_lst(n_lst)
    return l, r


def to_format_str(i, l, r):
    return str.format('Case #%d: %d %d\n' % (i, l, r))


file_input_name = 'C-small-1-attempt0.in'
file_output_name = 'C-small-1-attempt0.out'


if __name__ == '__main__':
    file_input = open(file_input_name, 'r')
    file_output = open(file_output_name, 'w')

    t = int(file_input.readline())

    for i in range(1, t + 1):
        data = file_input.readline()[:-1].split(' ')
        n = int(data[0])
        k = int(data[1])
        l, r = find_l_r_for_last_iter(n, k)
        file_output.write(to_format_str(i, l, r))
