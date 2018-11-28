from solver import solver


def gen(s):
    for x, y in zip(s, s[1:]):
        if x > y:
            yield chr(ord(x)-1)
            return
        yield x
    yield s[-1]


def reduce(n):
    s = str(n)
    return int(''.join(gen(s)).ljust(len(s), '9'))


@solver
def tidy(lines):
    n = int(lines[0])
    while reduce(n) != n:
        n = reduce(n)
    return n


if __name__ == '__main__':
    tidy.from_cli()
