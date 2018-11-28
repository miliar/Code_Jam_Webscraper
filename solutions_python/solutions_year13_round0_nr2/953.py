import sys


class Prob2(object):
    def __init__(self, mat):
        self.mat = mat
        self.output = "YES"

    def solve(self):
        for i in xrange(len(self.mat)):
            for j in xrange(len(self.mat[i])):
                if self.mat[i][j] != min(max(mat[i]), max([mat[x][j] for x in xrange(len(mat))])):
                    self.output = "NO"
                    break
        return self.output

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        line = f.readline()
        row, columns = [int(i) for i in line.strip().split(" ")]
        mat = []
        for k in xrange(row):
            line = f.readline()
            mat.append([int(i) for i in line.strip().split(" ")])

        p = Prob2(mat)
        print output % (counter+1, p.solve())
