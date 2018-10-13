__author__ = 'davidborsodi'


def solve(fap):
    c, f, x = map(float, fap.split())

    rate = 2.0
    nofarm = x/rate
    base = 0.0
    best = nofarm

    while True:
        base += c/rate
        rate += f
        candidate = base + x/rate
        if candidate >= best:
            break
        best = candidate
    return best


if __name__ == '__main__':
    lines = [line.rstrip() for line in open('12in')]
    case = 1
    inputs = lines[1:]
    out = open('12out', 'w')
    for i in inputs:
        print >> out, 'Case #{c}: {res}'.format(c=case, res=solve(i))
        case += 1
    out.close()
