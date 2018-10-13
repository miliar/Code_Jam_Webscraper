import sys

counter = 0

class Solver(object):
    def __init__(self, val):
        self.d = {}
        self.val = val

    def add(self, folder, val):
        paths = folder.split('/')[1:]
        self.add_(paths, 0, val)

    def add_(self, paths, idx, val):
        if idx >= len(paths):
            return 0
        if paths[idx] not in self.d:
            self.d[paths[idx]] = Solver(val)
        self.d[paths[idx]].add_(paths, idx+1, val)

    def add_existing(self, path):
        self.add(path, 1)

    def add_new(self, path):
        self.add(path, 0)

    def solve(self):
        global counter
        for path, obj in self.d.iteritems():
            if obj.val == 0:
                obj.val = 1
                counter +=1
            obj.solve()
        return counter


def main():
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        m, n = [int(x) for x in sys.stdin.readline().strip().split()]
        global counter
        counter = 0
        s = Solver(1)
        for j in range(m):
            s.add_existing(sys.stdin.readline().strip())
        for j in range(n):
            s.add_new(sys.stdin.readline().strip())
        print "Case #%d:" % (i+1), s.solve()

if __name__ == "__main__":
    main()
