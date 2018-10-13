#!/usr/bin/env python
QUAT = {
    '11': '1',
    '1i': 'i',
    '1j': 'j',
    '1k': 'k',
    'i1': 'i',
    'ii': '-1',
    'ij': 'k',
    'ik': '-j',
    'j1': 'j',
    'ji': '-k',
    'jj': '-1',
    'jk': 'i',
    'k1': 'k',
    'ki': 'j',
    'kj': '-i',
    'kk': '-1',
    'i': 'i',
    'j': 'j',
    'k': 'k'
}


def multiply(term):
    # print 'multiply:', term
    if '-' in term:
        term = term.replace('-', '')
        res = QUAT[term]
        if '-' in res:
            return res.replace('-', '')
        else:
            return '-' + res
    else:
        return QUAT[term]


def reduce(s):
    res = ''
    for c in s:
        res += c
        res = multiply(res)
    return res


def validate(s, reps):
    if len(s) == 1:
        return False

    string = s * reps
    cursor = 0

    i_found = False
    res = ''
    for i, c in enumerate(string):
        if res == 'i':
            cursor = i
            i_found = True
            break

        res += c
        res = multiply(res)

    if not i_found:
        return False

    j_found = False
    res = ''
    string = string[cursor:]
    for i, c in enumerate(string):
        if res == 'j':
            cursor = i
            j_found = True
            break

        res += c
        res = multiply(res)

    if not j_found:
        return False

    string = string[cursor:]
    return reduce(string) == 'k'


if __name__ == '__main__':
    with open('small.in', 'r') as infile:
        with open('small-output.txt', 'w') as outfile:
            cases = int(infile.readline().strip())

            for i in range(cases):
                line = infile.readline().strip()
                num_chars, reps = line.split()
                s = infile.readline().strip()
                valid = validate(s, int(reps))
                outfile.write(
                    'Case #{}: {}\n'.format(i + 1, 'YES' if valid else 'NO'))
