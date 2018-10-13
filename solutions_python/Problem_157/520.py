
def multiply(char1, char2):
    if char1 == '1':
        return (1, char2)

    if char2 == '1':
        return (1, char1)

    if char1 == char2:
        return (-1, '1')

    if char1 == 'i':
        if char2 == 'j':
            return (1, 'k')
        else:
            return (-1, 'j')

    if char1 == 'j':
        if char2 == 'i':
            return (-1, 'k')
        else:
            return (1, 'i')

    if char1 == 'k':
        if char2 == 'i':
            return (1, 'j')
        elif char2 == 'j':
            return (-1, 'i')


def reduces_to_minus1(sign, prefix, times, st):
    times_left = times
    current = '1'
    cur_sign = 1
    cur_pref = prefix

    while times_left > 0 or len(cur_pref) > 0:
        if len(cur_pref) == 0:
            cur_pref = st
            times_left -= 1

        n_s, current = multiply(current, cur_pref[0])
        cur_pref = cur_pref[1:]
        cur_sign *= n_s

    return cur_sign == sign and current == '1'


def reduces_to_i(sign, prefix, times, st):
    times_left = times
    current = '1'
    cur_sign = 1
    cur_pref = prefix

    while times_left > 0 or len(cur_pref) > 0:
        if len(cur_pref) == 0:
            cur_pref = st
            times_left -= 1

        n_s, current = multiply(current, cur_pref[0])
        cur_pref = cur_pref[1:]
        cur_sign *= n_s

    return cur_sign == sign and current == 'i'


def reduces_to_k(sign, prefix, times, st):
    times_left = times
    current = '1'
    cur_sign = 1
    cur_pref = prefix

    while times_left > 0 or len(cur_pref) > 0:
        if len(cur_pref) == 0:
            cur_pref = st
            times_left -= 1

        n_s, current = multiply(current, cur_pref[0])
        cur_pref = cur_pref[1:]
        cur_sign *= n_s

    return cur_sign == sign and current == 'k'


def reduces_to_jk(sign, prefix, times, st):
    times_left = times
    current = '1'
    cur_sign = sign
    cur_pref = prefix

    while times_left > 0 or len(cur_pref) > 0:
        if len(cur_pref) == 0:
            cur_pref = st
            times_left -= 1

        n_s, current = multiply(current, cur_pref[0])
        cur_pref = cur_pref[1:]
        cur_sign *= n_s

        if current == 'j' and cur_sign == sign:#reduces_to_k(cur_sign, cur_pref, times_left, st):
            return True

    return False


def reduces_to_ijk(sign, prefix, times, st):
    times_left = times
    current = '1'
    cur_sign = sign
    cur_pref = prefix

    while times_left > 0 or len(cur_pref) > 0:
        if len(cur_pref) == 0:
            cur_pref = st
            times_left -= 1

        n_s, current = multiply(current, cur_pref[0])
        cur_pref = cur_pref[1:]
        cur_sign *= n_s

        if current == 'i' and reduces_to_jk(cur_sign, cur_pref, times_left, st):
            return True

    return False


def solve_problem(X, st):
    return reduces_to_minus1(-1, '', X, st) and reduces_to_ijk(1, '', X, st)


if __name__ == '__main__':
    with open('d:\_Projects\GoogleCodeJam\inp\C-small-attempt1.in', 'r') as inp_file:
        all_lines = inp_file.readlines()
    all_lines = [x.replace('\n', '') for x in all_lines]

    n = int(all_lines[0])
    tasks = []
    i = 1
    while i < len(all_lines):
        L = all_lines[i].split(' ')[0]
        X = int(all_lines[i].split(' ')[1])

        tasks.append((X, all_lines[i+1]))
        i += 2

    #solve_problem(tasks[2][0], tasks[2][1])
    with open('d:\_Projects\GoogleCodeJam\inp\OUT_C-small-attempt1.out', 'w+') as out_file:
        for i in range(len(tasks)):
            print('Task', i+1)
            res = solve_problem(tasks[i][0], tasks[i][1])
            str_out = 'YES' if res else 'NO'
            out_file.write('Case #{0}: {1}\n'.format(i+1, str_out))