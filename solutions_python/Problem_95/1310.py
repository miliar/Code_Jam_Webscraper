import sys


def solve_line(line):
    translation_map = {
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
        'o': 'k',  # o, z
        'm': 'l',
        'x': 'm',
        's': 'n',
        'e': 'o',
        'v': 'p',
        'z': 'q',  # o, z
        'p': 'r',
        'd': 's',
        'r': 't',
        'j': 'u',
        'g': 'v',
        't': 'w',
        'h': 'x',
        'a': 'y',
        'q': 'z',
    }
    result = ''

    for char in line:
        if char in translation_map:
            result += translation_map[char]
        else:
            result += char

    return result


def process_results(results):
    with open('problem_a_solution.txt', 'w') as f:
        for i, r in enumerate(results):
            f.write('Case #%d: %s' % (i+1, r))


def main():
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]

        results = []

        for line in lines:
            results.append(solve_line(line))
            process_results(results)


if __name__ == '__main__':
    main()
