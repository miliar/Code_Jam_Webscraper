#inpath = "in.txt"
inpath = "A-small-attempt0.in"
outpath = "out.txt"

single = lambda f, c: c(f.readline().strip("\n"))
multi = lambda f, c: [c(s) for s in f.readline().split()]
case = lambda f, n, c: f.write("Case #%d: %s\n" % (n, " ".join(map(str, c))))

infile = open(inpath, "r")
outfile = open(outpath, "w")

trans = """
a y
b h
c e
d s
e o
f c
g v
h x
i d
j u
k i
l g
m l
n b
o k
p r
q z
r t
s n
t w
u j
v p
w f
x m
y a
z q
"""

trans = trans.split('\n')[1:-1]
trans = [t.split(' ') for t in trans]
trans.append([' ', ' '])
trans = dict(trans)

T = single(infile, int)
for i in range(T):
    G = single(infile, str)
    S = "".join(trans[c] for c in G)
    case(outfile, i + 1, [S])

infile.close()
outfile.close()
