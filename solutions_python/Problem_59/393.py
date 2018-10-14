import sys

class Tree(object):

    def __init__(self):
        self._t = {}

    def add(self, path):
        d = self._t
        c = 0
        for n in path:
            if n not in d:
                c += 1
            d = d.setdefault(n, {})
        return c

    def add_count(self, path):
        return self.add(path)

def doit(dirs, new_dirs):
    t = Tree()
    for d in dirs:
        s = d.split("/")
        assert s[0] == ""
        t.add(s[1:])
    c = 0
    for d in new_dirs:
        s = d.split("/")
        assert s[0] == ""
        c += t.add_count(s[1:])
    return c

if len(sys.argv) == 1:
    filename = "t.in"
else:
    filename = sys.argv[1]
f = open(filename)
f_out = open(filename[:-2] + "out", "w")
T = int(f.readline())
for i in range(T):
    N, M = [int(x) for x in f.readline().split()]
    dirs = []
    for j in range(N):
        dirs.append(f.readline().strip())
    new_dirs = []
    for j in range(M):
        new_dirs.append(f.readline().strip())
    s = "Case #%d: %s" % (i+1, doit(dirs, new_dirs))
    print s
    f_out.write(s + "\n")
