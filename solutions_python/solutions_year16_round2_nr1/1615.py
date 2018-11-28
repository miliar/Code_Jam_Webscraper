import q
import sys; sys.setrecursionlimit(1500000)


def _strip_data(data):
    return [x.strip() for x in data.readlines()[1:]]


def _write_output(completed_data, out_file):
    out_lines = ['Case #{}: {}\n'.format(i+1, line) for i, line in enumerate(completed_data)]
    out_file.writelines(out_lines)


def coding_challenge_specific_io(challenge_function):
    with open('input') as in_file:
        parsed_data = _parse_data(_strip_data(in_file))
    completed_data = [challenge_function(data) for data in parsed_data]
    q(completed_data)
    with open('output', 'w') as out_file:
        _write_output(completed_data, out_file)


@q
def _parse_header(header_line):
    header_data = header_line.split()
    header = {'end_line':0, 'data':header_data}
    return header


@q
def _parse_line(line):
    return [int(x) for x in line.split()]


def _parse_data(in_lines):
    if not in_lines: 
        return []
    header = _parse_header(in_lines[0])
    end = header['end_line']
    single_test = [_parse_line(line) for line in in_lines[1:end+1]]
    remaining_parsed_data = _parse_data(in_lines[end+1:])
    return [{'header':header, 'data':single_test}] + remaining_parsed_data


def func(x):
    words = [["ZERO", '0'], ["ONE", '1'], ["TWO", '2'], ["THREE", '3'], ["FOUR", '4'], ["FIVE", '5'], ["SIX", '6'], ["SEVEN", '7'], ["EIGHT", '8'], ["NINE", '9']]
    garbled = x['header']['data'][0]
    for x in range(len(words)):
        y = try_letters(words[x:], list(garbled))
        if y:
            return y


def try_letters(words, garbled):
    garbled = garbled[:]
    if not garbled:
        return True

    for letter in words[0][0]:
        if letter not in garbled:
            return False
        else:
            garbled.remove(letter)

    for x in range(len(words)):
        win_case = try_letters(words[x:], garbled)
        if win_case:
            if win_case == True:
                return words[0][1]
            else:
                return words[0][1] + win_case
    return False


if __name__=='__main__':
    #example
    coding_challenge_specific_io(func)


