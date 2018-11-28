from collections import OrderedDict, Counter

input_file = "A-small-attempt7.in"
output_file = "the_repeater.out"

cases = []
with open(input_file, 'r') as f:
    n_cases = int(f.readline())

    for i in range(n_cases):
        num_strings = int(f.readline())

        strings = []
        for i in range(num_strings):
            strings.append(f.readline().strip('\n'))
        
        cases.append(strings)


def char_sequence(string):
    result = [string[0]]
    for char in string:
        if char != result[-1]:
            result.append(char)

    return "".join(result)


def is_solveable(strings):
    base_sequence = char_sequence(strings[0])

    for string in strings:
        if base_sequence != char_sequence(string):
            return False

    return True


def str_distance(str1, str2):
    sequence = char_sequence(str1)

    str1, str2 = list(str1), list(str2)

    str1_lengths = []
    cur_length = 1
    for i in range(len(str1) - 1):
        if str1[i] == str1[i + 1]:
            cur_length += 1
        else:
            str1_lengths.append(cur_length)
            cur_length = 1
    str1_lengths.append(cur_length)

    str2_lengths = []
    cur_length = 1
    for i in range(len(str2) - 1):
        if str2[i] == str2[i + 1]:
            cur_length += 1
        else:
            str2_lengths.append(cur_length)
            cur_length = 1
    str2_lengths.append(cur_length)

    distance = 0
    for i in range(len(str1_lengths)):
        distance += abs(str1_lengths[i] - str2_lengths[i])


    return distance


def solve(strings):
    if not is_solveable(strings):
        return 'Fegla Won'

    return str_distance(strings[0], strings[1])


with open(output_file, 'w') as f:
    for case_number, case in enumerate(cases):
        answer = solve(case)

        f.write('Case #{case_number}: {answer}\n'.format(case_number=case_number + 1, answer=answer))
