

e_to_g = {'a': 'y',
          'b': 'n',
          'c': 'f',
          'd': 'i',
          'e': 'c',
          'f': 'w',
          'g': 'l',
          'h': 'b',
          'i': 'k',
          'j': 'u',
          'k': 'o',
          'l': 'm',
          'm': 'x',
          'n': 's',
          'o': 'e',
          'p': 'v',
          'q': 'z',
          'r': 'p',
          's': 'd',
          't': 'r',
          'u': 'j',
          'v': 'g',
          'w': 't',
          'x': 'h',
          'y': 'a',
          'z': 'q'}
g_to_e = {v:k for k, v in e_to_g.items()}


def parse_input(file):
    input_data = []
    with open(file, 'r') as f:
        total_cases = int(f.readline())
        for i in range(1, total_cases + 1):
            case = f.readline().split()
            input_data.append(case)
    return input_data


def translate_googlerese(data):
    r = []
    s = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            s.append(''.join([g_to_e[c] for c in data[i][j]]))
        r.append(' '.join(s))
        s = []
    return r


def main():
    d = parse_input('A-small-attempt0.in')
    t = translate_googlerese(d)
    total_cases = len(d)

    if not (0 <= total_cases <= 100):
        raise ValueError('Test case count out of range! Limits: 1 <= Count <= 100')

    with open('output.out', 'w') as output:
        for c in range(total_cases):
            output.write('Case #{}: {}\n'.format(c + 1, t[c]))
    print 'saving to file...'


if __name__ == '__main__':
    main()
