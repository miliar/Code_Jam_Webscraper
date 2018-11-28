import sys


def get_line(line, format):
    types = {
        'i': int,
        'f': float,
        's': str,
    }
    line = line.strip().split(' ')
    assert len(line) == len(format)
    for i, t in enumerate(format):
        line[i] = types[t](line[i])
    return tuple(line)


def solve(p, k):
    p = list(p)
    ans = 0
    for i in range(len(p)-k+1):
        if p[i] == '-':
            ans += 1
            for j in range(i, i+k):
                if p[j] == '-':
                    p[j] = '+'
                else:
                    p[j] = '-'
    if '-' in p:
        return 'IMPOSSIBLE'
    return ans


def main():
    next(sys.stdin)
    for i, l in enumerate(sys.stdin):
        p, k = get_line(l, 'si')
        print('Case #%d: %s' % (i+1, solve(p, k)))


if __name__ == '__main__':
    main()
