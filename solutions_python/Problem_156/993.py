import os, sys
from math import ceil
from collections import namedtuple
PancakeState = namedtuple('PancakeState', 'clock moves pancakes initial')


class LineReader:
    def __init__(self, file_name=None):
        if file_name is None:
            self.in_file = sys.stdin
        else:
            self.in_file = open(file_name)

    def read_line(self, *types, all=None):
        words = self.in_file.readline().strip().split()
        if len(types) == 0:
            if all is None:
                return words
            else:
                return [all(w) for w in words]
        assert (len(words) == len(types))
        if len(types) == 1:
            return types[0](words[0])
        return [types[i](w) for i, w in enumerate(words)]


class CaseWriter:
    def __init__(self, file_name=None, verbose=False):
        if file_name is None:
            self.out_file = sys.stdout
        else:
            self.out_file = open(file_name, 'w')
        self.case_idx = 1
        self.verbose = True

    def write_case(self, output):
        pfx = "Case #%d:" % self.case_idx
        self.case_idx += 1
        if isinstance(output, list):
            text = "\n".join([pfx] + output)
        else:
            text = pfx + ' ' + str(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            print(text)
        else:
            print(pfx)


class ReadWrite(LineReader):
    def __init__(self, in_file, verbose=False):
        super().__init__(in_file)
        output_name = os.path.splitext(in_file)[0] + '.out'
        self.writer = CaseWriter(output_name, verbose)

    def write_case(self, output):
        self.writer.write_case(output)


_best_moves = {}

def get_relevant(pancakes):
    return tuple(pancakes)
    m = pancakes[-1]
    if m<4:
        return (m, )
    return tuple([p for p in pancakes if p > 2])

def eat(pancakes):
    return tuple([p-1 for p in pancakes if p > 1])


def move_n(pancakes, n):
    s = pancakes[-1]
    assert (n<s)
    pancakes = list(pancakes[:-1]) + [n, s - n]
    pancakes.sort()
    return tuple(pancakes)

def find_max_multiplicity(pancakes):
    mx = pancakes[-1]
    i = len(pancakes) - 1
    while i >= 0 and pancakes[i] == mx:
        i -= 1
    return len(pancakes) -1 - i


def find_num_geq(pancakes, min_val):
    i = len(pancakes) - 1
    while i >= 0 and pancakes[i] >= min_val:
        i -= 1
    return len(pancakes) -1 - i

def get_best_moves(pancakes):
    print(len(pancakes), end=' ')
    mx = pancakes[-1]
    if mx<4:
        return mx * ['e']
    p = get_relevant(pancakes)
    try:
        return _best_moves[p]
    except KeyError:
        pass
    N = find_max_multiplicity(pancakes)
    if N>=mx//2:
        return mx * ['e']
    all_moves = []
    for n in range(2, mx//2+1):
        m = [str(n)] + get_best_moves(move_n(pancakes, n))
        all_moves.append((len(m), m))
    m = ['e'] + get_best_moves(eat(pancakes))
    all_moves.append((len(m), m))
    all_moves.sort()
    mn= all_moves[0][0]
    candidates = [m[1] for m in all_moves if m[0] == mn]
    for c in candidates:
        if c[0]=='e':
            return c
    return c



class PancakeHouse:
    def __init__(self, pancakes):
        self.pancakes = pancakes
        self.pancakes.sort()
        self.best_moves = get_best_moves(pancakes)
        self.best_clock = len(self.best_moves)

if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'B-small-attempt3.bin'
    rw = ReadWrite(input_name)
    T = rw.read_line(int)
    for t in range(T):
        D = rw.read_line(int)
        pancakes = rw.read_line(all=int)
        assert (D==len(pancakes))
        ph = PancakeHouse(pancakes)
        print(ph.pancakes)
        print(ph.best_moves)
        rw.write_case(ph.best_clock)
