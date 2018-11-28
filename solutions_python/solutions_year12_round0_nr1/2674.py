language = {'a': 'y',
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
            'z': 'q'}


def translate(sentence):
    translated = []
    for letter in sentence:
        if letter in language:
            tr = language[letter]
            translated.append(tr)
        else:
            translated.append(letter)
    return ''.join(translated)


if __name__ == '__main__':
    number = raw_input()
    try:
        num = int(number)
        if num < 1 or num > 30:
            raise ValueError
        cases = []
        for i in xrange(0, num):
            case = raw_input()
            cases.append(case)
        for i, case in enumerate(cases):
            tr = translate(case)
            print "Case #%d: %s" % (i + 1, tr)
    except ValueError:
        print "Invalid input case number!"
