import os, re, sys
from collections import namedtuple
from copy import deepcopy


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
        self.out_file.write(text+'\n')
        if self.verbose:
            print(text)
        else:
            print(pfx)


class ReadWrite(LineReader):
    def __init__(self, in_file, verbose=False):
        super().__init__(in_file)
        output_name = os.path.splitext(input_name)[0] + '.out'
        self.writer = CaseWriter(output_name, verbose)

    def write_case(self, output):
        self.writer.write_case(output)


class Audience:
    def __init__(self, shyness):
        self.shyness = shyness
        self.sorted_shyness = list(self.shyness.keys())
        self.sorted_shyness.sort()
        self.min_invite = self.calculate_min_invite()

    def calculate_min_invite(self):
        standing = 0
        total = 0
        self.need={}
        self.need_if_all={}
        for s in self.sorted_shyness:
            if s<standing:
                self.need[s] = s - standing
                self.need_if_all[s] = s - total
            else:
                self.need[s] = 0
                self.need_if_all[s] = s - total
                standing += self.shyness[s]
            total += self.shyness[s]
        return max(self.need_if_all.values())

if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'A-small-practice.bin'
    rw = ReadWrite(input_name, verbose=True)
    T = rw.read_line(int)
    for t in range(T):
        smax, a = rw.read_line(int, str)
        shyness = {s: int(n) for s, n in enumerate(a) if int(n)>0}
        audience = Audience(shyness)
        rw.write_case(audience.min_invite)
