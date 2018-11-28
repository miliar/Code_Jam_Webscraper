# python 2.7

import os, sys

class Input:
    def __init__(self, fp): self.fp = fp
    def m(self, n, t=str):  return [map(t, list(self.line())) for i in range(n)]
    def ms(self, n, t=str, sep=' '):  return [map(t, self.line().split(sep)) for i in range(n)]
    def line(self):  return self.fp.readline().strip()
    def lines(self, n): return [self.fp.readline().strip() for x in range(n)]
    def words(self): return self.line().split()
    def int(self):   return int(self.line())
    def ints(self):  return map(int, self.words())
    def float(self): return float(self.line())
    def floats(self):return map(float, self.words())
    def str(self):   return self.line()
    def types(self, *types): return [t(w) for t,w in zip(types, self.words())]

if __name__ == "__main__":

    fn = "test.txt" if len(sys.argv) <= 1 else sys.argv[1]
    f = Input(open(fn))
    fout = open(os.path.splitext(fn)[0] + ".out", "w")

    def answer(t, ans):
        o = "Case #%d: %s\n"%(t, ans)
        sys.stdout.write(o)
        fout.write(o)

    import itertools
    def rle(s):
        return [(v, sum(1 for x in g)) for (v, g) in itertools.groupby(s)]

    def error_sum(l, v):
        return sum(abs(x - v) for x in l)

    for case in range(f.int()):
        N = f.int()
        lines = f.lines(N)

        b = None

        seqs = []
        counts = []
        for line in lines:
            s, c = zip(*rle(line))
            seqs.append(tuple(s))
            counts.append(c)

        if len(set(seqs)) > 1:
            answer(case + 1, "Fegla Won")
            continue

        # another transpose to index by char, not line
        counts = zip(*counts)

        moves = 0
        for cc in counts:
            avg = sum(cc) / len(cc)
            aa = error_sum(cc, avg)
            bb = error_sum(cc, avg + 1)
            moves += min(aa, bb)

        answer(case + 1, moves)
