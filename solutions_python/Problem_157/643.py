import sys

__author__ = 'Via'

# f = open('example_input.txt')
f = open('C-small-attempt3.in')
# f = open('A-large-practice.in')
total_case = int(f.readline().strip())
file_out = open('output3.txt', 'a')

matrix = {}
matrix['11'] = '1'
matrix['1i'] = 'i'
matrix['1j'] = 'j'
matrix['1k'] = 'k'

matrix['i1'] = 'i'
matrix['ii'] = '-1'
matrix['ij'] = 'k'
matrix['ik'] = '-j'

matrix['j1'] = 'j'
matrix['ji'] = '-k'
matrix['jj'] = '-1'
matrix['jk'] = 'i'

matrix['k1'] = 'k'
matrix['ki'] = 'j'
matrix['kj'] = '-i'
matrix['kk'] = '-1'


def find_matrix(row, col):
    if row == col:
        ret = '-1'
    elif row == '1' and col == '1':
        ret = '1'
    elif ('-' in row) and ('-' in col):
        ret = matrix[row.replace('-', '') + col.replace('-', '')]
    elif ('-' in row) and ('-' not in col):
        ret = '-' + matrix[row.replace('-', '') + col]
    elif ('-' not in row) and ('-' in col):
        ret = '-' + matrix[row + col.replace('-', '')]
    else:
        ret = matrix[row + col]

    if '--' in ret:
        return ret.replace('--', '')
    else:
        return ret


def find_char(p_str, p, c):
    if p >= len(p_str): return -1
    if p_str[p] == c:
        return p + 1

    trans = p_str[p]
    for idx in range(p + 1, len(p_str)):
        trans = find_matrix(trans, p_str[idx])
        if trans == c:
            return idx + 1
    return sys.maxint*-1


def is_k(p_str, idx_j):
    trans = p_str[idx_j]
    for idx in range(idx_j + 1, len(p_str)):
        trans = find_matrix(trans, p_str[idx])
    if trans == 'k':
        return True
    else:
        return False


def solve(p_str):
    orig_str = p_str[:]
    result = 'NO'
    idx_i = find_char(orig_str, 0, 'i')
    while idx_i >= 0 and result == 'NO':
        idx_j = find_char(orig_str, idx_i, 'j')
        while idx_j > 0 and result == 'NO':
            if is_k(orig_str, idx_j):
                result = 'YES'
                return result
            else:
                # find another j after current idx_j
                if orig_str[idx_j-1] == 'j':
                    p_str_j =orig_str[idx_j:]
                else:
                    p_str_j = 'j' + orig_str[idx_j:]
                if p_str_j == orig_str or len(p_str_j) == 1:
                    return result
                idx_j += find_char(p_str_j, 0, 'j')

        # can't find j so find another i after current idx_i
        if orig_str[idx_i-1] == 'i':
            p_str_i = orig_str[idx_i:]
        else:
            p_str_i = 'i' + orig_str[idx_i:]
        if p_str_i == orig_str or len(p_str_i) == 1:
            return result
        idx_i += find_char(p_str_i, 0, 'i')

    return result

def simple_solve(p_str):
    orig_str = p_str[:]
    result = 'NO'
    idx_i = find_char(orig_str, 0, 'i')
    if idx_i >= 0:
        idx_j = find_char(orig_str, idx_i, 'j')
        if idx_j > 0:
            if is_k(orig_str, idx_j):
                return 'YES'

    return result

# print find_matrix('-i', '-i')
# print solve('ijjk')

for i in range(total_case):
    c, repeat = map(int, f.readline().split())
    ss = f.readline().strip('\n')
    p_str = ''
    for r in range(repeat):
        p_str += ss

    result = simple_solve(p_str)
    print 'Case #{}: {}'.format(i + 1, result)
    file_out.writelines('Case #{}: {}\n'.format(i + 1, result))

file_out.close()