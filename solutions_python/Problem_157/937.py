from itertools import product

__author__ = 'jakub.bibro'

global already_computer
global already_computer_ind

def findSplit(letter_to_reduce, start_index, letters, multi_map):
    results = []
    current = letters[start_index]
    if current == letter_to_reduce:
        results.append(start_index)

    if start_index > len(letters) - 1:
        return []
    for ind, letter in enumerate(letters[start_index:-1]):
        current = multi_map[(current, letters[ind + start_index + 1])]
        # print(current)
        if current == letter_to_reduce:
            results.append(ind + start_index + 1)

    return results


def checkIfLettersReduceToK(start_index, letters, multi_map):
    global already_computer_ind
    global already_computer

    if start_index >= len(letters):
        return False

    current = letters[start_index]
    if current == 'k' and start_index == len(letters) - 1:
        return True

    for ind, letter in enumerate(letters[start_index:already_computer_ind]):
        current = multi_map[(current, letters[ind + start_index + 1])]

    if already_computer_ind < -1:
        already_computer_ind = start_index - len(letters) - 1
        current = mult_map[(current, already_computer)]
        already_computer = current
    else:
        already_computer = current
        already_computer_ind = start_index - len(letters) - 1

    if current == 'k':
        return True

    return False


def solve(letters, mult_map):
    global already_computer_ind
    split_i = findSplit('i', 0, letters, mult_map)
    # print split_i
    if len(split_i) == 0:
        return 'NO'

    split_j = findSplit('j', split_i[0] + 1, letters, mult_map)
    # print split_j
    if len(split_j) == 0:
        return 'NO'

    for single_split_i in split_i:
        already_computer_ind = -1

        # splits_j = findSplit('j', single_split_i + 1, letters, mult_map)

        split_j_valid = [s for s in split_j if s > single_split_i]
        for single_split_j in reversed(split_j_valid):
            if checkIfLettersReduceToK(single_split_j + 1, letters, mult_map):
                # print 'computer for ', single_split_j + 1
                # print single_split_i
                # print single_split_j
                return 'YES'


    return 'NO'

def validateMap(multi_map):
    letters = ['i', 'j', 'k', '1', '-1', '-i', '-j', '-k']

    for pair in product(letters, repeat=2):
        print(pair)
        if multi_map[(pair[0], pair[1])] != multi_map[('-' + pair[0] if pair[0][0] != '-' else pair[0][1:], '-'+pair[1] if pair[1][0] != '-' else pair[1][1:])]:
            print('BAD')
        if multi_map[('-'+pair[0] if pair[0][0] != '-' else pair[0][1:], pair[1])] != multi_map[(pair[0], '-'+pair[1] if pair[1][0] != '-' else pair[1][1:])]:
            print('BAD')
        if multi_map[(pair[0], '-'+pair[1] if pair[1][0] != '-' else pair[1][1:])] != multi_map[('-'+pair[0] if pair[0][0] != '-' else pair[0][1:], pair[1])]:
            print('BAD')


if __name__ == '__main__':
    already_computer_ind = -1
    already_computer = 'xx'
    mult_map = {}

    mult_map[('1', '1')] = '1'
    mult_map[('1', '-1')] = '-1'
    mult_map[('1', 'i')] = 'i'
    mult_map[('1', '-i')] = '-i'
    mult_map[('1', 'j')] = 'j'
    mult_map[('1', '-j')] = '-j'
    mult_map[('1', 'k')] = 'k'
    mult_map[('1', '-k')] = '-k'

    mult_map[('-1', '1')] = '-1'
    mult_map[('-1', '-1')] = '1'
    mult_map[('-1', 'i')] = '-i'
    mult_map[('-1', '-i')] = 'i'
    mult_map[('-1', 'j')] = '-j'
    mult_map[('-1', '-j')] = 'j'
    mult_map[('-1', 'k')] = '-k'
    mult_map[('-1', '-k')] = 'k'

    mult_map[('i', '1')] = 'i'
    mult_map[('i', '-1')] = '-i'
    mult_map[('i', 'i')] = '-1'
    mult_map[('i', '-i')] = '1'
    mult_map[('i', 'j')] = 'k'
    mult_map[('i', '-j')] = '-k'
    mult_map[('i', 'k')] = '-j'
    mult_map[('i', '-k')] = 'j'

    mult_map[('-i', '1')] = '-i'
    mult_map[('-i', '-1')] = 'i'
    mult_map[('-i', 'i')] = '1'
    mult_map[('-i', '-i')] = '-1'
    mult_map[('-i', 'j')] = '-k'
    mult_map[('-i', '-j')] = 'k'
    mult_map[('-i', 'k')] = 'j'
    mult_map[('-i', '-k')] = '-j'

    mult_map[('j', '1')] = 'j'
    mult_map[('j', '-1')] = '-j'
    mult_map[('j', 'i')] = '-k'
    mult_map[('j', '-i')] = 'k'
    mult_map[('j', 'j')] = '-1'
    mult_map[('j', '-j')] = '1'
    mult_map[('j', 'k')] = 'i'
    mult_map[('j', '-k')] = '-i'

    mult_map[('-j', '1')] = '-j'
    mult_map[('-j', '-1')] = 'j'
    mult_map[('-j', 'i')] = 'k'
    mult_map[('-j', '-i')] = '-k'
    mult_map[('-j', 'j')] = '1'
    mult_map[('-j', '-j')] = '-1'
    mult_map[('-j', 'k')] = '-i'
    mult_map[('-j', '-k')] = 'i'

    mult_map[('k', '1')] = 'k'
    mult_map[('k', '-1')] = '-k'
    mult_map[('k', 'i')] = 'j'
    mult_map[('k', '-i')] = '-j'
    mult_map[('k', 'j')] = '-i'
    mult_map[('k', '-j')] = 'i'
    mult_map[('k', 'k')] = '-1'
    mult_map[('k', '-k')] = '1'

    mult_map[('-k', '1')] = '-k'
    mult_map[('-k', '-1')] = 'k'
    mult_map[('-k', 'i')] = '-j'
    mult_map[('-k', '-i')] = 'j'
    mult_map[('-k', 'j')] = 'i'
    mult_map[('-k', '-j')] = '-i'
    mult_map[('-k', 'k')] = '1'
    mult_map[('-k', '-k')] = '-1'
    # validateMap(mult_map)
    test_cases = int(raw_input())
    for i in range(0, test_cases):
        repeat_num = int(raw_input().split(' ')[1])
        single_letters = [l for l in raw_input()]
        letters = single_letters * repeat_num
        solution = solve(letters, mult_map)
        print('Case #{}: {}'.format(i + 1, solution))

