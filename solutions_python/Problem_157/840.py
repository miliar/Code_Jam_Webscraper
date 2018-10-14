class Quat:
    quats = {}

    def __init__(self, name, front, back):
        self.name = name
        self.front = front
        self.back = back

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __mul__(self, other):
        if other is None:
            return self, 1

        if self is other:
            return None, -1

        if other.name == self.back:
            return self.quats[self.front], -1

        if other.name == self.front:
            return self.quats[self.back], 1

    def __rmul__(self, other):
        if other is None:
            return self, 1


Quat.quats.update({
    'i': Quat('i', front='j', back='k'),
    'j': Quat('j', front='k', back='i'),
    'k': Quat('k', front='i', back='j')
})

i = Quat.quats['i']
j = Quat.quats['j']
k = Quat.quats['k']


def find_i(s):
    sign_value = 1

    value = Quat.quats[s[0]]

    if value is i:
        return s[1:]

    for index, c in enumerate(s[1:]):
        if c not in 'ijk':
            break

        value, sign = value * Quat.quats[c]
        sign_value *= sign

        if value is i and sign_value == 1:
            return s[index + 2:]


def find_k(s):
    sign_value = 1

    s = s[::-1]

    value = Quat.quats[s[0]]

    if value is k:
        return s[1:][::-1]

    for index, c in enumerate(s[1:]):
        if c not in 'ijk':
            break

        value, sign = Quat.quats[c] * value
        sign_value *= sign

        if value is k and sign_value == 1:
            return s[index + 2:][::-1]


def match_j(s):
    if len(s) == 0:
        return False

    sign_value = 1
    value = Quat.quats[s[0]]

    for c in s[1:]:
        if c not in 'ijk':
            break

        value, sign = value * Quat.quats[c]
        sign_value *= sign

    return value is j and sign_value == 1


def is_it_possible(s, multiplier):
    full_s = s * multiplier

    k_string = find_i(full_s)

    if k_string is None:
        return False

    j_string = find_k(k_string)

    if j_string is None:
        return False

    return match_j(j_string)


def compute_result(input_file, output_file):
    with open(input_file) as file, open(output_file, 'w') as result_file:
        nr_of_tests = int(file.readline())

        for case in range(1, nr_of_tests + 1):
            test_line = file.readline()
            _, x = test_line.split(sep=' ')

            multiplier = int(x)

            s = ''.join([c for c in file.readline() if c in 'ijk'])

            possible = is_it_possible(s, multiplier)

            result_file.write('Case #%d: %s\r\n' % (case, 'YES' if possible else 'NO'))


if __name__ == '__main__':
    compute_result('C-small-attempt0.in', 'result.txt')
