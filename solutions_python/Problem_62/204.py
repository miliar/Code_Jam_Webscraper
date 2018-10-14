"""
Framework for Google code jam
  (c) 2010, Nicolas Dumazet <nicdumz@gmail.com>

Released under WTFPL, have fun with it.
"""
import sys
import itertools

fin = fout = None
try:
    fname = sys.argv[1]
    fin = open(fname, 'r')
    fout = open("%s.out" % fname.split(".")[0], 'w')
except IndexError:
    raise ValueError("Please give a filename on commandline")

class Solver(object):
    def __init__(self, lines_per_problem=1):
        self.n = lines_per_problem
        self.lines = fin
        self.size = int(self.lines.next())
        self.problem = 0

    def __iter__(self):
        return self

    def _fetch(self, nb):
        return list(itertools.islice(self.lines, nb))

    def next(self):
        """List of lines for each problem"""
        l = self._fetch(self.n)
        if not l:
            raise StopIteration
        return l

    def answer(self, answer):
        """Answer current problem"""
        self.problem += 1
        if not isinstance(answer, (list, tuple)):
            answer = [answer]
        s = "Case #%d: %s" % (self.problem, " ".join(map(str, answer)))
        print >> fout, s
        print >> sys.stderr, s

    def check_size(self):
        assert self.problem == self.size, \
                "not answered all problems? (answered:%s, size:%s)" \
                % (self.problem, self.size)

class Solver2(Solver):
    def next(self):
        l = self._fetch(1)
        if not l:
            raise StopIteration
        n = mint(l[0])
        return self._fetch(n[0])


def mint(line):
    return map(int, line.split())
def mfloat(line):
    return map(float, line.split())


s = Solver2(1)
for lines in s:
    wires = [mint(l) for l in lines]
    nb = 0
    for i, wire in enumerate(wires):
        l, r = wire
        for wire2 in wires[i+1:]:
            l2,r2 = wire2
            if l2 > l:
                if r2 < r:
                    nb +=1
            else:
                if r2 > r:
                    nb +=1
    
    s.answer(nb)

s.check_size()
