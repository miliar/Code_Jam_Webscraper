__author__ = "Jungkyu Park"
__email__ = "parkssie@gmail.com"


def last_tidynumber(str_x: int) -> int:
    rv = 0
    int_x = int(str_x)

    for i in range(int_x, -1, -1):
        tmp_x = list(map(int, list(str(i))))
        if is_tidy(tmp_x):
            rv = i
            break
    return rv


def is_tidy(list_int_x: list) -> bool:
    rv = True
    len_x = len(list_int_x) - 1
    for i in range(len_x, -1, -1):
        if i > 0:
            if list_int_x[i] - list_int_x[i - 1] >= 0:
                rv = True
            else:
                rv = False
                break
    return rv


if __name__ == '__main__':

    result_list = []
    with open('./B-small-attempt0.in', 'r') as file:
        seq = 0
        seq_max = 1
        for line in file:

            input_string = line.replace('\n', '')
            if seq == 0:
                seq_max = int(input_string)
            else:
                input_val = int(input_string)
                output = last_tidynumber(int(input_val))
                result = 'Case #{}: {}'.format(seq, output)
                result_list.append(result)

            if seq > seq_max:
                break
            seq += 1

    with open('./B-small-attempt0.out', 'w') as file:
        for result in result_list:
            file.write('{}\n'.format(result))
