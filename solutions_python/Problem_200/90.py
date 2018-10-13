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
    return tuple(line) if len(line) > 1 else line[0]


class Problem:
    def __init__(self, x):
        self.x = x

    def dfs(self, state, depth, bounded):
        if len(state) == len(self.x):
            return state
        max_digit = self.x[depth] if bounded else 9
        min_digit = state[-1] if len(state) > 0 else 0
        for d in range(max_digit, min_digit-1, -1):
            state.append(d)
            ans = self.dfs(state, depth+1, bounded and (d == max_digit))
            if ans is not None:
                return ans
            state.pop()
        return None

    def solve(self):
        self.x = list(str(self.x))
        self.x = list(map(int, self.x))

        ans = self.dfs([], 0, True)
        ans = int(''.join(list(map(str, ans))))
        return ans


def main():
    sys.stdin = open('B-large.in', 'r')
    sys.stdout = open('b.out', 'w')
    next(sys.stdin)
    for i, l in enumerate(sys.stdin):
        x = get_line(l, 'i')
        p = Problem(x)
        print('Case #%d: %s' % (i+1, p.solve()))


if __name__ == '__main__':
    main()
