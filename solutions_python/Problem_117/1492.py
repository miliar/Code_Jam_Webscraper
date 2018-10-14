#!/usr/bin/python


class Lawn:
    def __init__(self, h, w, l):
        self.cache = [{}, {}]
        self.mark = [{}, {}]
        self.lawn = l
        self.height = h
        self.width = w

    # direction: 0 for horizontal, 1 for vertical
    def checkline(self, direction, n):
        if n in self.cache[direction]:
            return self.cache[direction][n]

        if n in self.mark[direction] and self.mark[direction][n]:
            return False

        line = []

        size = 0
        if direction == 0:
            size = self.width
            for i in range(size):
                line.append(self.lawn[n][i])
        else:
            size = self.height
            for i in range(size):
                line.append(self.lawn[i][n])

        maxn = max(line)

        for i in range(size):
            if line[i] != maxn:
                self.mark[direction][n] = True
                if not self.checkline(0 if direction else 1, i):
                    self.cache[direction][n] = False
                    self.mark[direction][n] = False
                    return False
                self.mark[direction][n] = False

        self.cache[direction][n] = True
        return True

    def check(self):
        for i in range(self.height):
            if not lawn.checkline(0, i):
                return False

        for i in range(self.width):
            if not lawn.checkline(1, i):
                return False

        return True


n = int(raw_input())
lawns = []

for _ in range(n):
    lawn = []
    dim = raw_input().split(' ')
    nrows = int(dim[0])
    ncols = int(dim[1])

    for _ in range(nrows):
        lawn.append(raw_input().split(' '))

    lawns.append(Lawn(nrows, ncols, lawn))

i = 0
for lawn in lawns:
    i += 1
    if lawn.check():
        print "Case #%d: %s" % (i, "YES")
    else:
        print "Case #%d: %s" % (i, "NO")
