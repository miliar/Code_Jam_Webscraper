# pylint: disable=missing-docstring
import sys


def problem(case):
    N, R, O, Y, G, B, V = [int(x) for x in case.split(" ")]
    B -= O
    R -= G
    Y -= V
    if R < 0 or Y < 0 or B < 0:
        return 'IMPOSSIBLE'

    res = ''
    left = {
        'R': R,
        'Y': Y,
        'B': B
    }
    if max(left.values()) == 0:
        res = ''
    else:
        res = max(left.keys(), key=lambda x: left[x])
        left[res] -= 1

    while sum(left.values()) > 0:
        possible = [x for x in left.keys() if x != res[-1]]
        choice = max(possible, key=lambda x: left[x] + (0.5 if res[0] == x else 0))
        if left[choice] < 1:
            return 'IMPOSSIBLE'
        left[choice] -= 1
        res += choice

    if len(res) > 2 and res[-1] == res[0]:
        return 'IMPOSSIBLE'

    if O > 0:
        if 'B' in res:
            return res.replace('B', 'B' + 'OB' * O, 1)
        if res == '':
            return 'OB' * O
        return 'IMPOSSIBLE'
    if G > 0:
        if 'R' in res:
            return res.replace('R', 'R' + 'GR' * G, 1)
        if res == '':
            return 'GR' * G
        return 'IMPOSSIBLE'
    if V > 0:
        if 'Y' in res:
            return res.replace('Y', 'Y' + 'VY' * V, 1)
        if res == '':
            return 'VY' * V
        return 'IMPOSSIBLE'
    return res


def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile)
            result += 'Case #{}: {}\n'.format(1 + run, problem(case))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
