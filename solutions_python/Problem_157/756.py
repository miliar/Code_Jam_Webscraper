import sys

mul_table = {'1': {'1': ('1', True), 'i': ('i', True), 'j': ('j', True), 'k': ('k', True)},
             'i': {'1': ('i', True), 'i': ('1', False), 'j': ('k', True), 'k': ('j', False)},
             'j': {'1': ('j', True), 'i': ('k', False), 'j': ('1', False), 'k': ('i', True)},
             'k': {'1': ('k', True), 'i': ('j', True), 'j': ('i', False), 'k': ('1', False)}
             }

def mul(a, b):
    res = mul_table[a][b]
    return res[1], res[0] # sign(False for neg), val

def get_char(i, L, L_len):
    """
    :param i: the number we want
    :param L: the string of characters
    :return:
    """
    return L[i % L_len]

def works(state, idx, input_str, L_X, debug=False):
    L_len = len(input_str)

    val = get_char(idx, input_str, L_len)
    minuses = 0
    for i in xrange(idx+1, L_X+1):
        curr_char = get_char(i, input_str, L_len)
        if debug:
            print 'examining %s * %s for finding %s idx %d' % (val, curr_char, state, i)

        sign, val = mul(val, curr_char)
        if not sign:
            minuses += 1

        if val == state and minuses % 2 == 0:
            if state == 'i':
                return works('j', i+1, input_str, L_X)
            elif state == 'j':
                return works('k', i+1, input_str, L_X)
            elif state == 'k' and i < L_X - 1: # 0 based indexing
                continue
            elif state == 'k' and i == L_X - 1:
                return True

    return False


with open(sys.argv[1], 'r') as input:
    num_cases = int(input.readline())
    f_out = open('dijkstra.out', 'w+')
    for k in xrange(1, num_cases+1):
        L, X = [int(x) for x in input.readline().split()]
        L_X = L*X
        input_str = input.readline()[:L]
        if L_X < 3:
            f_out.write('Case #%d: NO\n' % (k,))
            continue
        if input_str == 'ijk' and X == 1:
            f_out.write('Case #%d: YES\n' % (k,))
            continue

        if works('i', 0, input_str, L_X):
            f_out.write('Case #%d: YES\n' % (k,))
        else:
            f_out.write('Case #%d: NO\n' % (k,))

    f_out.close()



