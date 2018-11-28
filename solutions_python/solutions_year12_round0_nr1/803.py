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
        if len(fields) != k:
            raise Exception('expected {}, found {} fields in {}'.format(k, len(fields), line))
        return [typ(f) for f in fields]
    

def main():
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

if __name__ == "__main__":
    main()
