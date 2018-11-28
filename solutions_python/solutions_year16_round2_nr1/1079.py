def generate_digits(s):
    m = {}
    for c in s:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

    r_map = {}
    result = ''
    if 'Z' in m and m['Z'] != 0:
        c = m['Z']
        r_map[0] = c
        m['Z'] -= c
        m['E'] -= c
        m['R'] -= c
        m['O'] -= c

    if 'W' in m and m['W'] != 0:
        c = m['W']
        r_map[2] = c
        m['W'] -= c
        m['T'] -= c
        m['O'] -= c

    if 'U' in m and m['U'] != 0:
        c = m['U']
        r_map[4] = c
        m['U'] -= c
        m['F'] -= c
        m['O'] -= c
        m['R'] -= c

    if 'X' in m and m['X'] != 0:
        c = m['X']
        r_map[6] = c
        m['X'] -= c
        m['S'] -= c
        m['I'] -= c

    if 'G' in m and m['G'] != 0:
        c = m['G']
        r_map[8] = c
        m['G'] -= c
        m['E'] -= c
        m['I'] -= c
        m['H'] -= c
        m['T'] -= c

    if 'O' in m and m['O'] != 0:
        c = m['O']
        r_map[1] = c
        m['O'] -= c
        m['N'] -= c
        m['E'] -= c

    if 'H' in m and m['H'] != 0:
        c = m['H']
        r_map[3] = c
        m['H'] -= c
        m['H'] -= c
        m['R'] -= c
        m['E'] -= c * 2

    if 'F' in m and m['F'] != 0:
        c = m['F']
        r_map[5] = c
        m['I'] -= c
        m['F'] -= c
        m['V'] -= c
        m['E'] -= c

    if 'V' in m and m['V'] != 0:
        c = m['V']
        r_map[7] = c
        m['V'] -= c
        m['S'] -= c
        m['N'] -= c
        m['E'] -= c * 2

    if 'E' in m and m['E'] != 0:
        c = m['E']
        r_map[9] = c
        m['E'] -= c
        m['N'] -= c * 2
        m['I'] -= c

    for i in range(10):
        if i in r_map:
            result += r_map[i] * str(i)

    return result


if __name__ == '__main__':
    # s = 'NEOZRINE'
    # print generate_digits(s)

    f = open('1.in')
    f1 = open('A.out', 'wb')
    T = f.readline()

    i = 1
    for l in f.readlines():
        f1.write('Case #' + str(i) + ': ' + generate_digits(l.strip()) + '\n')
        i += 1

    f.close()
    f1.close()
