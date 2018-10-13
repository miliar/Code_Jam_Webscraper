import argparse, sys

code = {'a': 'y', ' ': ' ', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

alphabet = 'abcdefghijklmnopqrstuvwxyz'
assert len(alphabet) == 26

missing_keys = set([c for c in alphabet]).difference(set(code.keys()))
missing_values = set([c for c in alphabet]).difference(set(code.values()))
assert len(missing_keys) == 0
assert len(missing_values) == 0

def learn(input_file, output_file):
    input_lines = []
    output_lines = []
    n = 0

    with open(input_file) as f:
        n = int(f.readline())
        input_lines = [l for l in f]
    with open(output_file) as f:
        output_lines = [l.split(':')[1].strip() for l in f]

    result = {}
    for i in range(0, n):
        input_line = input_lines[i]
        output_line = output_lines[i]
        result.update(dict(zip(input_line, output_line)))

    print str(result)

def solve(input_file):
     with open(input_file) as f:
        n = int(f.readline())
        for i in range(0, n):
            result = [code[c] for c in f.readline() if c != '\n']
            print 'Case #%d: %s' % (i+1, ''.join(result),)

def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--learn', action='store_true', default=False)
    parser.add_argument('--solve', action='store_true', default=False)
    parser.add_argument('files', nargs='+', type=str)
    arguments = parser.parse_args(args)

    if arguments.learn:
        learn(*arguments.files)
    if arguments.solve:
        solve(arguments.files[0])


if __name__ == '__main__':
    sys.exit(main())
