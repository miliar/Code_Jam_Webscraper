import sys


def evaluate(counts):
    current = 0
    additional = 0

    for s_i, count in enumerate(counts):
        recruited = max(0, s_i - current)
        additional += recruited
        current += count + recruited

    return additional


if __name__ == '__main__':
    sys.stdin.readline()  # skip case count

    for i, line in enumerate(sys.stdin):
        _, digits = line.split(' ')
        counts = map(int, digits.strip())
        print 'Case #{0}: {1}'.format(i + 1, evaluate(counts))
