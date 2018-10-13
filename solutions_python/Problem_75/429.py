#! /usr/bin/python
# GCJ 2011 QR - Magicka

from sys import stdin


def parse_test_case(line) :
    tokens = line.strip().split(' ')

    n_combos = int(tokens.pop(0))
    combos = {}
    for i in range(0, n_combos) :
        [base1, base2, result] = tokens.pop(0)
        combos[(base1, base2)] = result
        combos[(base2, base1)] = result

    n_opposites = int(tokens.pop(0))
    opposites = dict([(l, []) for l in 'QWERASDF'])
    for i in range(0, n_opposites) :
        [base1, base2] = tokens.pop(0)
        opposites[base1].append(base2)
        opposites[base2].append(base1)

    invocation = tokens[1]

    return (combos, opposites, invocation)


def cast_spell(combos, opposites, invocation) :
    current_spell = []

    for s in invocation :
        current_spell.append(s)

        if len(current_spell) >= 2 :
            c = (current_spell[-1], current_spell[-2])
            if c in combos :
                current_spell[-2:] = combos[c]
                continue

        for o in current_spell[:-1] :
            if o in opposites[s] :
                current_spell = []
                break

    return current_spell


def print_output(test_id, solution) :
    solution_str = str(solution).replace('\'', '')
    print('Case #{0}: {1}'.format(test_id, solution_str))


def main() :
    input_data = stdin.readlines()

    n_tests = int(input_data[0])
    for i in range(1, n_tests + 1) :
        test_data = parse_test_case(input_data[i])
        solution = cast_spell(*test_data)
        print_output(i, solution)

if __name__ == '__main__' :
    main()
