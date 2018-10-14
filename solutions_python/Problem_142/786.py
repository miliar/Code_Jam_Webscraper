from optparse import OptionParser
import math


def unify(sample):
    if not sample:
        return ''
    used_chars = []
    current_char = None
    for character in sample:
        if not current_char or character is not current_char[0]:
            if current_char:
                used_chars.append(current_char)
            current_char = [character, 1]
        else:
            current_char[1] += 1
    used_chars.append(current_char)
    return used_chars


def sums(i, strings):
    sum = 0
    for string in strings:
        sum += string[i][1]
    return sum / len(strings)


def moves(i, target, strings):
    sum = 0
    for string in strings:
        sum += abs(target - string[i][1])
    return sum


def solve_case(input_file):
    number_of_strings = int(input_file.readline())
    strings = []
    for _ in range(number_of_strings):
        strings.append(input_file.readline().strip())
    if not strings:
        return '0'
    used_chars_array = []
    one_string = None
    for string in strings:
        used_chars_array.append(unify(string))
        if not one_string:
            one_string = ''.join([x[0] for x in used_chars_array[-1]])
        else:
            test_string = ''.join([x[0] for x in used_chars_array[-1]])
            if one_string != test_string:
                return 'Fegla Won'
    used_moves = 0
    for i in range(len(one_string)):
        difference = sums(i, used_chars_array)
        moves_one = moves(i, math.floor(difference), used_chars_array)
        moves_two = moves(i, math.ceil(difference), used_chars_array)
        used_moves += min(moves_one, moves_two)
    return str(used_moves)


def process_files(input_file, output_file):
    number_of_cases = int(input_file.readline())
    for case in range(number_of_cases):
        result = solve_case(input_file)
        output_file.write('Case #%i: %s\n' % (case + 1, result))


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='inputFile',
                      help='test case file', metavar='FILE')
    parser.add_option('-o', '--output', dest='outputFile',
                      help='result file', metavar='FILE')
    (options, args) = parser.parse_args()

    if not options.inputFile or not options.outputFile:
        parser.error("options -i and -o are not optional")
    else:
        process_files(open(options.inputFile, 'r'), open(options.outputFile, 'w'))