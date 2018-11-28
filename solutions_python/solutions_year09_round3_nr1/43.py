import sys

from string import whitespace, digits




def get_next_case(inp):
    T = int(inp.readline())
    for t in xrange(T):
        line = inp.readline()[:-1]
        yield line


def get_min_seconds(line):
    mapping = {}
    symbols = set(line)
    base = len(symbols) if len(symbols) > 1 else 2

    mapping[line[0]] = 1
    nums = [0] + range(2, base)

    for c in line[1:]:
        if c not in mapping:
            mapping[c] = nums.pop(0)

    seconds = 0
    length = len(line)
    for n, c in enumerate(line):
        seconds += mapping[c] * pow(base, length - n - 1)

    return seconds


def main():
    assert len(sys.argv) == 3, "%s inpfile outpfile" % sys.argv[0]

    inp = open(sys.argv[1], 'rt')
    outp = open(sys.argv[2], 'wt')

    for n, line in enumerate(get_next_case(inp)):
        outp.write('Case #%d: %d\n' % (n+1, get_min_seconds(line)))

    inp.close()
    outp.close()


if __name__ == '__main__':
    main()

