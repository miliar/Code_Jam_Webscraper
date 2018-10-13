
def decode(str):
    mapping = {
        'y': 'a',
        'n': 'b',
        'f': 'c',
        'i': 'd',
        'c': 'e',
        'w': 'f',
        'l': 'g',
        'b': 'h',
        'k': 'i',
        'u': 'j',
        'o': 'k',
        'm': 'l',
        'x': 'm',
        's': 'n',
        'e': 'o',
        'v': 'p',
        'z': 'q',
        'p': 'r',
        'd': 's',
        'r': 't',
        'j': 'u',
        'g': 'v',
        't': 'w',
        'h': 'x',
        'a': 'y',
        'q': 'z',
        ' ': ' ',
        '\n': ''
    }

    decoded = ''
    for i in str:
        decoded += mapping[i]

    return decoded


input_file = open("input.txt", "r")
input_lines_count = int(input_file.readline())
line_index = 0

result = ''
while line_index < input_lines_count:
    input_line = input_file.readline()
    line_no = line_index + 1
    result += "Case #" + str(line_no) + ": " + decode(input_line) + "\n"
    line_index += 1

output_file = open("result.txt", "w")
output_file.writelines(result)
output_file.close()
