import sys
from collections import Counter


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
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def dfs(self, counter):
        intervals = counter.items().sort()
        new_counter = Counter()
        print(intervals)

    def solve(self):
        counter = Counter({self.n: 1})
        while True:
            intervals = sorted(counter.items(), reverse=True)
            # print(intervals)
            new_counter = Counter()
            for length, cnt in intervals:
                new_counter[int(length/2)] += cnt
                new_counter[int((length-1)/2)] += cnt
                self.k -= cnt
                if self.k <= 0:
                    return '%d %d' % (int(length/2), int((length-1)/2))
                counter = new_counter
        return None


def main():
    sys.stdin = open('C-small-2-attempt0.in', 'r')
    sys.stdout = open('c.out', 'w')
    next(sys.stdin)
    for i, l in enumerate(sys.stdin):
        n, k = get_line(l, 'ii')
        p = Problem(n, k)
        print('Case #%d: %s' % (i+1, p.solve()))


if __name__ == '__main__':
    main()
