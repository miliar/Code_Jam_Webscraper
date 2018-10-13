def fix_order(big_number):
    change_index = len(big_number) - 1
    ordered = False
    while change_index >= 0 and not ordered:
        if big_number[change_index]:
            big_number[change_index] -= 1
        else:
            big_number[change_index] = 9
        change_index -= 1
        ordered = False if change_index > -1 and \
            big_number[change_index] > big_number[change_index + 1] else True
        if not ordered:
            big_number.pop()
    return big_number, change_index + 1


def solution(number):
    previous = 0
    result = []
    nines = 0
    for ch_index in xrange(0, len(number)):
        digit = int(number[ch_index])
        if previous > digit:
            result, last_change = fix_order(result)
            nines = len(number) - last_change - 1
            break
        previous = digit
        result.append(digit)
    return (''.join(map(str, result)) + (nines * '9')).lstrip('0')

files = [
    # 'B-small-attempt2.in',
    # 'test.in',
    'B-large.in'
]

if __name__ == '__main__':
    for filename in files:
        outfilename = filename.replace('.in', '.out')
        with open(filename, 'r') as f:
            with open(outfilename, 'w') as w:
                no_lines = int(f.readline())
                results = []
                for index in xrange(0, no_lines):
                    N = f.readline()
                    print 'Processing case {}'.format(index + 1)
                    result = solution(N.strip('\n'))
                    w.writelines("Case #{}: {}\n".format(index +1, result))
