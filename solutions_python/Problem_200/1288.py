def is_tidy(x):
    s = str(x)
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return False
    return True


def last_tidy_number(n):
    while 1:
        print n
        if is_tidy(n):
            return n
        i = 1
        while 1:
            if n % (10 ** i) < 10 ** i - 1:
                n -= 10 ** (i - 1)
                break
            i += 1


def process(filename):
    answers = []
    with open(filename + '.in') as f:
        lines = tuple(f.readlines())
    cases = int(lines[0])
    for x in range(1, cases + 1):
        n = int(lines[x])
        answers.append('Case #{}: {}'.format(x, last_tidy_number(n)))
    with open(filename + '.out', 'w') as f:
        f.write('\n'.join(answers))


if __name__ == '__main__':
    process('B-sample')
    process('B-small-attempt0')
    process('B-large')
