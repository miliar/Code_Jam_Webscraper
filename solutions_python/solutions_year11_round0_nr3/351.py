import operator

def cry(xs):
    return reduce(operator.xor, xs)

def solve(xs):
    if cry(xs):
        return 'NO'
    return sum(xs) - min(xs)

if __name__ == '__main__':
    import sys
    it = iter(sys.stdin)
    next(it)
    for i, (_, line) in enumerate(zip(it, it), 1):
        xs = map(int, line.split())
        print 'Case #{}: {}'.format(i, solve(xs))
