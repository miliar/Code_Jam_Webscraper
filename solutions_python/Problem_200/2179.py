
import sys
import logging
from pprint import pformat

log = logging.getLogger()
logging.basicConfig(level=logging.WARN)


def get_input():
    with open(sys.argv[1], 'r') as f:
        return f.readlines()[1:]


def is_tidy(nl):
    m = nl[0]
    for v in nl[1:]:
        if v < m:
            return False
        m = v
    return True


def dec(nl, i):
    log.debug('dec({}, {})'.format(nl, i))
    if nl[i] > 0:
        nl[i] -= 1
    else:
        if i == 0:
            raise ValueError('Cant Decrement 0')
        nl[i] = 9
        dec(nl, i-1)


def nines(nl, i):
    for j in range(i, len(nl)):
        nl[j] = 9


def solve(n):
    log.debug('SOLVE: {}'.format(n))
    nl = map(int, list(str(n)))
    while not is_tidy(nl):
        log.debug('Step: {}'.format(nl))
        m = nl[0]
        for i, v in enumerate(nl):
            if i == 0:
                continue
            if v < m:
                dec(nl, i-1)
                nines(nl, i)
                break
            m = v
    return int(''.join(map(str, nl)))


def main():
    lines = get_input()
    for i, line in enumerate(lines):
        n = int(line)
        r = solve(n)
        print('Case #{}: {}'.format(i + 1, r))


if __name__ == '__main__':
    main()
