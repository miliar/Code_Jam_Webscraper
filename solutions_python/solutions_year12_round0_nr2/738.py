import sys

g_to_e = '''
a	y
b	h
c	e
d	s
e	o
f	c
g	v
h	x
i	d
j	u
k	i
l	g
m	l
n	b
o	k
p	r
q	z
r	t
s	n
t	w
u	j
v	p
w	f
x	m
y	a
z	q
'''

# read k elements separated by sep, and convert them to type typ
class Reader:
    def __init__(self, filename, sep = ' ', typ = int):
        self.sep = sep
        self.typ = typ
        self.in_file = open(filename)
        
    def get_line(self):
        return next(self.in_file).rstrip()

    def next(self, k = 1, sep = None, typ = None):
        line = self.get_line()
        if typ is None:
            typ = self.typ
        if k == 1:
            return typ(line)
        if sep is None:
            sep = self.sep
        fields = line.split(sep)
        if k != 0 and len(fields) != k:
            raise Exception('expected {}, found {} fields in {}'.format(k, len(fields), line))
        return [typ(f) for f in fields]


def problem1():
    it = iter(g_to_e.splitlines())
    d = {}
    for line in it:
        line = line.rstrip()
        if line == '':
            continue
        g, e = line.split('\t')
        d[g] = e
    d[' '] = ' '
    r = Reader(sys.argv[1], sep = None)
    n = r.next()
    for t in range(1, n+1):
        s = r.next(typ = str)
        result = ''.join(d[c] for c in s)
        print('Case #{}: {}'.format(t, result))


Feasible = 0
FeasibleButSurprising = 1
Infeasible = 2

def feasible(s, threshold):
    if threshold + max(0, threshold-1) * 2 <= s:
        return Feasible
    if threshold + max(0, threshold-2) * 2 <= s:
        return FeasibleButSurprising
    return Infeasible

def problem2():
    r = Reader(sys.argv[1])
    n_tests = r.next()
    for t in range(1, n_tests+1):
        n_googlers, n_surprising, threshold, *scores = r.next(k = 0)
        result = 0
        for s in scores:
            assessment = feasible(s, threshold)
            if assessment == Feasible:
                result += 1
                continue
            if assessment == FeasibleButSurprising:
                if n_surprising > 0:
                    n_surprising -= 1
                    result += 1
        print('Case #{}: {}'.format(t, result))


def main():
    problem2()

if __name__ == "__main__":
    main()
