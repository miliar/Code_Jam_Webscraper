from math import log


def empty_stalls(n, k):
    x = 2 ** (1 + int(log(k, 2)))
    return (n - k % (x // 2)) // x, (n - k) // x


def process(filename):
    answers = []
    with open(filename + '.in') as f:
        lines = tuple(f.readlines())
    t = int(lines[0])
    for i in range(1, t + 1):
        n, k = map(int, lines[i].split())
        max_spaces, min_spaces = empty_stalls(n, k)
        answers.append('Case #{}: {} {}'.format(i, max_spaces, min_spaces))
    with open(filename + '.out', 'w') as f:
        f.write('\n'.join(answers))


if __name__ == '__main__':
    # process('C-sample')
    # process('C-small-1-attempt2')
    process('C-small-2-attempt1')
    # process('C-large')
