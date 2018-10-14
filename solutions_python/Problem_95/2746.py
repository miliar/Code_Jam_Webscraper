import fileinput

TRANS_MAP = {
            'a': 'y',
            'b': 'h',
            'c': 'e',
            'd': 's',
            'e': 'o',
            'f': 'c',
            'g': 'v',
            'h': 'x',
            'i': 'd',
            'j': 'u',
            'k': 'i',
            'l': 'g',
            'm': 'l',
            'n': 'b',
            'o': 'k',
            'p': 'r',
            'q': 'z',
            'r': 't',
            's': 'n',
            't': 'w',
            'u': 'j',
            'v': 'p',
            'w': 'f',
            'x': 'm',
            'y': 'a',
            'z': 'q',
            }


def translate(line):
    tline = ''
    for letter in line:
        try:
            tline += TRANS_MAP[letter]
        except KeyError:
            tline += letter
    return tline


num_cases = 0
for index, line in enumerate(fileinput.input()):
    if index == 0:
        num_cases = line
    else:
        tline = translate(line)
        print('Case #%i: %s' % (index, tline))
