def eta(d, k, s):
    return (d - k) * 1.0 / s


def process(filename):
    answers = []
    with open(filename + '.in') as f:
        lines = tuple(f.readlines())
    t = int(lines[0])
    y = 1
    for x in range(1, t + 1):
        times = []
        d, n = map(int, lines[y].split())
        y += 1
        for i in range(n):
            k, s = map(int, lines[y].split())
            times.append(eta(d, k, s))
            y += 1
        speed = d * 1.0 / max(times)
        answers.append('Case #{}: {}'.format(x, speed))
    with open(filename + '.out', 'w') as f:
        f.write('\n'.join(answers))


if __name__ == '__main__':
    process('A-sample')
    process('A-small-attempt0')
    process('A-large')
