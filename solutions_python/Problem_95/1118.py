import sys

MAPPING = {
        ' ': ' ',
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


def translate_text(source):
    for s in source:
        yield MAPPING[s]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fd:
        fd.readline()

        for idx, line in enumerate(fd):
            line = translate_text(line.strip())

            print 'Case #%d: %s' % (idx + 1, ''.join(line))
