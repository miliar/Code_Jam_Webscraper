import sys
import functools
from collections import Counter

ijk_table = {
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
    ('k', 'k'): '-1'
}

def quaternion_equivelant(characters, lk=None, ax=0):
    cumul = '1'
    sign = 1

    for i, c in enumerate(characters):
        ad = ijk_table[(cumul, c)]

        if len(ad) > 1:
            sign *= -1
            cumul = ad[1]
        else:
            cumul = ad[0]

        if lk is not None and cumul == lk:
            return (i + ax, (sign, cumul))

    return (-2, (sign, cumul))

def is_correct_spelling(string):
    if len(string) < 3:
        return 'NO'

    i, fp = quaternion_equivelant(string, 'i')
    if i == -2:
        return 'NO'

    j, sp = quaternion_equivelant(string[i + 1:], 'j', i + 1)
    if j == -2:
        return 'NO'

    k, tp = quaternion_equivelant(string[j + 1:], 'k', j + 1)
    if k == -2:
        return 'NO'

    sign = fp[0] * sp[0] * tp[0]

    if k != len(string):
        if sign < 0:
            if quaternion_equivelant(string[k + 1:])[1] == (-1, '1'):
                return 'YES'
            else:
                return 'NO'
        else:
            if quaternion_equivelant(string[k + 1:])[1] == (1, '1'):
                return 'YES'
            else:
                return 'NO'
    else:
        return 'YES'

if __name__ == '__main__': 
    sys.stdin.readline()

    for i, line in enumerate(sys.stdin, 1):
        repeat = int(line.split()[1])

        line = sys.stdin.readline().strip()

        result = 'NO'
        if len(Counter(line)) > 1:
            result = is_correct_spelling(line * repeat)

        print("Case #{}: {}".format(i, result))

