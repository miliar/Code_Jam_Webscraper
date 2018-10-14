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


def digits(n):
    return [int(d) for d in str(n)]


def deltas(digits):
    # pad beginning with the first digit, so we always have at least one
    # delta > 0
    return [digits[0]] + [digits[i] - digits[i - 1]
                          for i in range(1, len(digits))]


def first_untidy_digit(deltas):
    for i, d in enumerate(deltas):
        if d < 0:
            return i
    return None


def make_tidy(digits, start_idx):
    result = [str(d) for d in digits[0:start_idx]]
    result.append(str(digits[start_idx] - 1))
    result.extend(['9'] * (len(digits) - start_idx - 1))
    return int("".join(result))


def solve(N):
    dig = digits(N)
    if len(dig) == 1:
        return N
    delt = deltas(dig)
    fud = first_untidy_digit(delt)
    if fud is None:
        return N
    # work backwards until we find a delta that's big enough to decrease
    # by 1
    for i in range(fud - 1, -1, -1):
        if delt[i] > 0:
            return make_tidy(dig, i)
            a

    # we didn't find a delta that's big enough.  This shouldn't happen.
    assert False


if __name__ == '__main__':

    input_name = sys.argv[1] if len(sys.argv) > 1 else 'B-tiny-practice.in'
    rw = ReadWrite(input_name)
    T = rw.read_line(int)
    for t in range(T):
        N = rw.read_line(int)
        rw.write_case(str(solve(N)))
