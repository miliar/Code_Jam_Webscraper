from itertools import (
    izip_longest,
)


# https://docs.python.org/3.3/library/itertools.html#itertools-recipes
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def main():
    input_file = open('C-small-attempt1.in', 'r')
    output_file = open('C-small-attempt1.out', 'w')
    input_list = list(input_file)
    number_of_test_cases = input_list[0]

    lines = iter(input_list[1:])
    test_case_number = 0
    for lx, chars in grouper(lines, 2):
        l, x = lx.split(' ')
        test_case_number += 1

        print('Working on case {} of {}'.format(test_case_number, number_of_test_cases))
        if eval_test_case(int(l), int(x.rstrip('\n')), chars.rstrip('\n')):
            #print ('Case #{}: YES'.format(test_case_number))
            output_file.write('Case #{}: YES\n'.format(test_case_number))
        else:
            #print('Case #{}: NO'.format(test_case_number))
            output_file.write('Case #{}: NO\n'.format(test_case_number))
    output_file.close()
    print('done!')


def eval_test_case(l, x, chars):
    #print('eval_test_case(l, x, chars): {}, {}, {}'.format(l, x, chars))
    found_i_index = (0, -1)
    found_j_index = (0, -1)

    searching_for_i = True
    searching_for_j = False
    searching_for_k = False
    searching_to_end = False

    last_j_return = -1

    cx = 1
    i = 0
    product = '1'
    while cx <= x:
        #print('  while cx <= x: {}, {}'.format(cx, x))
        while i < l:
            #print('    while i < l: {}, {}'.format(i, l))
            product = mult(product, chars[i])
            if searching_for_i and product == 'i':
                found_i_index = (cx, i)
                searching_for_i = False
                searching_for_j = True
                product = '1'
            if searching_for_j and product == 'j':
                found_j_index = (cx, i)
                searching_for_j = False
                searching_for_k = True
                product = '1'
            if searching_for_k and product == 'k':
                searching_for_k = False
                searching_to_end = True
                product = '1'
            i += 1

        at_end = cx == x
        if at_end and searching_for_k:
            # print('at_end and searching_for_k')
            # back up to last j
            cx = found_j_index[0]
            product = 'j'
            searching_for_k = False
            searching_for_j = True
        if at_end and searching_for_j:
            # print('at_end and searching_for_j')
            # back up to last i
            cx = found_i_index[0]
            product = 'i'
            searching_for_j = False
            searching_for_i = True
        if at_end and searching_for_i:
            # print('at_end and searching_for_i')
            return False
        if at_end and searching_to_end:
            # print('at_end and searching_to_end')
            if product == '1':
                return True
            else:
                # back up to last j
                cx = found_j_index[0]
                i = found_j_index[1]
                product = mult('j', chars[i])
                searching_to_end = False
                searching_for_k = True
                if i == last_j_return:
                    return False
                last_j_return = i
        i = 0
        cx += 1

    return False


def mult(a, b):
    #print('mult({}, {})'.format(a, b))
    sign_a = ''
    sign_b = ''

    if a[0] == '-':
        sign_a = '-'
        a = a[1]

    if b[0] == '-':
        sign_b = '-'
        b = b[1]

    sign = ''
    if sign_a != sign_b:
        sign = '-'

    truth_table = {
        '1': {
            '1': '1',
            'i': 'i',
            'j': 'j',
            'k': 'k',
        },
        'i': {
            '1': 'i',
            'i': '-1',
            'j': 'k',
            'k': '-j',
        },
        'j': {
            '1': 'j',
            'i': '-k',
            'j': '-1',
            'k': 'i',
        },
        'k': {
            '1': 'k',
            'i': 'j',
            'j': '-i',
            'k': '-1',
        },
    }

    product = truth_table[a][b]
    product_sign = ''
    if product.startswith('-'):
        product_sign = '-'

    if sign == '-' and product_sign == '-':
        sign = ''
        product = product[1:]

    return sign + product

main()



