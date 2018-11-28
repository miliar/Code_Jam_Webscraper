__author__ = "Jungkyu Park"
__email__ = "parkssie@gmail.com"


def t_test(s: str, k: int) -> int:
    list_s = list(s)
    len_s = len(list_s)
    flip_cnt = 0
    for x in range(0, len_s):
        if list_s[x] == '-':
            list_s[x:x + k] = flip(list_s[x:x + k])
            flip_cnt += 1
        # Finds 'IMPOSSIBLE'
        if (len_s - x - k == 0) and '-' in list_s:
            flip_cnt = -1
            break
    # print('result', list_s)
    return flip_cnt


def flip(s: str) -> str:
    rv = ''
    for x in range(0, len(s)):
        rv += '+' if s[x] == '-' else '-'
    return rv


if __name__ == '__main__':
    # s : happy side (+) / blank side (-)
    # k : size of flipper (K consecutive pancakes)
    # t : test case
    # output : count of fliping pancakes
    # result : formatted string (Case #x: y)

    result_list = []
    with open('./A-large.in', 'r') as file:
        seq = 0
        seq_max = 1
        for line in file:

            input_string = line.replace('\n', '')
            if seq == 0:
                seq_max = int(input_string)
            else:
                intput_s, input_k = input_string.split()
                t = t_test(intput_s, int(input_k))
                output = 'IMPOSSIBLE' if t == -1 else str(t)
                result = 'Case #{}: {}'.format(seq, output)
                result_list.append(result)

            if seq > seq_max:
                break
            seq += 1

    with open('./A-large.out', 'w') as file:
        for result in result_list:
            file.write('{}\n'.format(result))
