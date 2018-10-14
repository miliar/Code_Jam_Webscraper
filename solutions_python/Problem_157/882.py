import sys

readline = sys.stdin.readline

num_cases = int(readline())


MULT_TABLE = {
    ('1', '1'): '1',
    ('1', 'i'): 'i',
    ('1', 'j'): 'j',
    ('1', 'k'): 'k',

    ('i', '1'): 'i',
    ('i', 'i'): '-1',
    ('i', 'j'): 'k',
    ('i', 'k'): '-j',

    ('j', '1'): 'j',
    ('j', 'i'): '-k',
    ('j', 'j'): '-1',
    ('j', 'k'): 'i',

    ('k', '1'): 'k',
    ('k', 'i'): 'j',
    ('k', 'j'): '-i',
    ('k', 'k'): '-1',
}

# make negatives
for a_b, result in MULT_TABLE.items():
    a, b = a_b
    neg_result = result[1:] if '-' in result else '-' + result
    MULT_TABLE[('-' + a, b)] = neg_result
    MULT_TABLE[(a, '-' + b)] = neg_result
    MULT_TABLE[('-' + a, '-' + b)] = result


MEMO = {}
TARGETS = 'ijk'
TARGETS_END = -1


def memo_mult(chars, start, end):
    # key = (chars, start, end)
    main_key = chars[start:end+1]
    if main_key in MEMO:
        return MEMO[main_key]

    rv = chars[start]
    i = start + 1
    # skips if start == end
    while i <= end:
        key = chars[i:end+1]
        if key in MEMO:
            i = end
            c = MEMO[key]
        else:
            c = chars[i]
        rv = MULT_TABLE[(rv, c)]
        i += 1
    MEMO[main_key] = rv
    return rv


def find_char(chars, pos_start, neg_target_index):
    target = TARGETS[neg_target_index]
    pos_max = len(chars) + neg_target_index
    if neg_target_index == TARGETS_END:
        return memo_mult(chars, pos_start, pos_max) == target

    stop = pos_start
    while stop <= pos_max:
        if memo_mult(chars, pos_start, stop) == target:
            return find_char(chars, stop + 1, neg_target_index + 1)
        stop += 1
    return False




for i_case in xrange(1, num_cases + 1):
    # reset the memoization
    MEMO = {}
    _, repeat = readline().strip().split()
    chars = readline().strip() * int(repeat)
    ok = find_char(chars, 0, -3)
    print 'Case #%s: %s' % (i_case, 'YES' if ok else 'NO')
