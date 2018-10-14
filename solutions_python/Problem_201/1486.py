import collections
import sys

import os

sys.setrecursionlimit(500000)


class ReadWrite:
    def __init__(self, file_name=None, verbose=True):
        self.verbose = verbose
        if file_name is None:
            self.in_file = sys.stdin
            self.out_file = sys.stdout
        else:
            self.in_file = open(file_name)
            self.out_file = open(os.path.splitext(file_name)[0] + '.out', 'w')
        self.case_idx = 1

    def msg(self, output, end='\n'):
        sys.stderr.write(str(output) + end)

    def read_line(self, *types, all=None):
        words = self.in_file.readline().strip().split()
        if all is not None:
            return [all(w) for w in words]
        if len(types) == 0:
            return words
        assert (len(words) == len(types))
        if len(types) == 1:
            return types[0](words[0])
        return [t(w) for t, w in zip(types, words)]

    def write_case(self, output, true="YES", false="NO", join='\n'):
        pfx = "Case #%d:" % self.case_idx
        self.case_idx += 1
        if isinstance(output, list):
            text = join.join([pfx] + output)
        elif isinstance(output, bool):
            text = pfx + ' ' + (true if output else false)
        else:
            text = pfx + ' ' + str(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            self.msg(text)
        else:
            self.msg(pfx)


def split_intervals(max_k, intervals):
    new_i = collections.defaultdict(int)
    new_mk = max_k

    for k, v in intervals.items():
        if k == 1:
            new_mk += v
        elif k == 2:
            new_i[1] += v
            new_mk += v
        else:
            right = k // 2
            left = k - 1 - right
            new_i[right] += v
            new_i[left] += v
            new_mk += 2 * v

    return max_k, new_mk, new_i


def lr_interval(i):
    right = i // 2
    left = i - 1 - right
    return (right, left)


def solve(N, K):
    intervals = {N: 1}
    min_k = 0
    max_k = 1
    while not (min_k <= K <= max_k):
        min_k, max_k, intervals = split_intervals(max_k, intervals)
    k = min_k
    isizes = sorted(list(intervals.keys()))
    isizes.reverse()
    for i in isizes:
        n = intervals[i]
        if k + n >= K:
            return lr_interval(i)
        k += n
    assert False


if __name__ == '__main__':

    input_name = sys.argv[1] if len(sys.argv) > 1 else 'C-tiny-practice.in'
    rw = ReadWrite(input_name)
    T = rw.read_line(int)
    for t in range(T):
        N, K = rw.read_line(int, int)
        rw.write_case("%d %d" % solve(N, K))
