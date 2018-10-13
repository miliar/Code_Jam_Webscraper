import sys
import getopt
import os
import operator
from itertools import islice
from collections import defaultdict
from heapq import heappush, heappop


class GCJProblem(object):
    def __init__(self, inpath, outpath):
        self.inpath = inpath
        self.outpath = outpath
        self.debugwriter = sys.stdout if outpath else sys.stderr


    def solve_one(self, file):
        N, K = file.read_ints()
        intervals = [-N]
        ivdict = defaultdict(int)
        ivdict[N] = 1
        while True:
            # print(K, intervals, ivdict)
            i = -heappop(intervals)
            n = ivdict[i]
            if K == 0:
                return "0 0"
            if i % 2 == 0 and K <= n:
                return "{} {}".format(int(i / 2), int(i / 2) - 1)
            elif i % 2 == 1 and K <= n:
                return "{} {}".format(int(i / 2), int(i / 2))

            K -= n
            if i % 2 == 0:
                i1, i2 = int(i / 2) - 1, int(i / 2)
                if -i1 not in intervals:
                    heappush(intervals, -i1)
                if -i2 not in intervals:
                    heappush(intervals, -i2)
                ivdict[i2] += n
                ivdict[i1] += n
            else:
                i1 = int(i / 2)
                if -i1 not in intervals:
                    heappush(intervals, -i1)
                ivdict[i1] += n * 2

        # 0 9 --> next 4 (4, 3)
        # 0 4 9
        # 0 4 6 9 ->> next = 2 (1 1)
        # 0 7
        # 0 3 7
        # 0 3 5 7

    def solve(self):
        with InFileWrapper(self.inpath) as f, OutFileWrapper(self.outpath) as of:
            T = f.read_int()
            self.debug("Running [{}] Cases".format(T))

            for t in range(1, T + 1):
                res = self.solve_one(f)
                of.write_case(t)
                of.write_string(res)
                of.write_case_end()

    def debug(self, s):
        self.debugwriter.write("{}\n".format(s))


class FileWrapper(object):
    def __init__(self, path, mode):
        if path:
            self.file = open(path, mode)
        elif mode == 'r':
            self.file = sys.stdin
        elif mode == 'w':
            self.file = sys.stdout

    def close(self):
        self.file.close()

    def __enter__(self):
        """Return the wrapper when you enter this as a decorator."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """On decorator exit, close the wrapped file/stream."""
        self.close()


class InFileWrapper(FileWrapper):
    def __init__(self, path):
        FileWrapper.__init__(self, path, 'r')

    def read_chars(self, strip=True):
        return list(self.read_line(strip))

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return [int(z) for z in self.read_line().split()]

    def read_float(self):
        return float(self.file.read_line())

    def read_floats(self):
        return [float(z) for z in self.read_line().split()]

    def read_words(self):
        return self.read_line().split()

    def read_decimal(self):
        return [Decimal(d) for d in self.read_line().split()]

    def read_line(self, strip=True):
        if strip:
            return self.file.readline().strip()
        else:
            return self.file.readline()

    def read_grid(self, rows, read_func):
        return [read_func() for x in range(rows)]

    def skip_lines(self, n=1):
        for x in range(n):
            self.read_line()


class OutFileWrapper(FileWrapper):
    def __init__(self, path):
        FileWrapper.__init__(self, path, 'w')

    def write_case(self, n):
        self.file.write("Case #{}: ".format(n))
        return self

    def write_string(self, s):
        self.file.write(s)
        return self

    def write_decimal(self, d):
        self.file.write("{:.7f}".format(d))
        return self

    def write_case_end(self):
        self.file.write("\n")
        return self


def main():
    """Main function."""
    opts, args = getopt.gnu_getopt(sys.argv[1:], "fio", [])
    infile, outfile = None, None
    if '-f' in opts:
        infile = opts['-f']
        outfile = os.path.splitext(infile)[0] + ".out"
    elif '-i' in opts:
        infile = opts['-i']
        if '-o' in opts:
            outfile = opts['-o']

    GCJProblem(infile, outfile).solve()
    pass


if __name__ == "__main__":
    main()
