"""
Google Code Jam
2017 Round 1A

Problem A
    :author: yamaton
    :date: 2017-04-14
"""
import sys


def fill_line(s):
    if '?' not in s:
        return s
    elif set(s) == {'?'}:
        return s
    else:
        lett = s.replace('?', '')
        positions = [s.index(c) for c in lett] + [len(s)]
        intervals = [b - a for (a, b) in zip(positions, positions[1:])]
        out = ""
        for c, interval in zip(lett, intervals):
            out += c * interval
        return out.rjust(len(s), lett[0])


def solve(ss):
    lines = [fill_line(s) for s in ss]
    transposed = [''.join(line) for line in zip(*lines)]
    transposed = [fill_line(s) for s in transposed]
    backed = [''.join(line) for line in zip(*transposed)]
    return '\n'.join(backed)


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d:" % _tc, end='\n')
        r, c = map(int, input().split())
        ss = [input().strip() for _ in range(r)]
        assert len(ss[0]) == c

        result = solve(ss)
        pp()
        pp('ss =', ss)
        pp('result =')
        pp(result)
        print(result)


if __name__ == '__main__':
    main()
