

class Template:
    def process(self, fin, fout):
        [self.R, self.C] = [int(x) for x in fin.readline().strip().split()]
        self.data = [[] for _ in range(self.R)]
        for i in range(self.R):
            self.data[i] = [x for x in fin.readline().strip().split()[0]]

        for i in range(self.R):
            for j in range(self.C):
                self.deal_ud(i, j)

        for i in range(self.R):
            for j in range(self.C):
                self.deal_lr(i, j)

        self.print_cake(fout)

    def deal_ud(self, i, j):
        self.deal_up(i, j)
        self.deal_down(i, j)

    def deal_lr(self, i, j):
        self.deal_left(i, j)
        self.deal_right(i, j)

    def deal_up(self, i, j):
        init = self.data[i][j]
        if init == '?':
            return
        for x in reversed(range(i)):
            if self.data[x][j] != '?':
                return
            self.data[x][j] = init

    def deal_down(self, i, j):
        init = self.data[i][j]
        if init == '?':
            return
        for x in range(i + 1, self.R):
            if self.data[x][j] != '?':
                return
            self.data[x][j] = init

    def deal_right(self, i, j):
        init = self.data[i][j]
        if init == '?':
            return
        for x in range(j + 1, self.C):
            if self.data[i][x] != '?':
                return
            self.data[i][x] = init

    def deal_left(self, i, j):
        init = self.data[i][j]
        if init == '?':
            return
        for x in reversed(range(j)):
            if self.data[i][x] != '?':
                return
            self.data[i][x] = init

    def print_cake(self, fout):
        for r in self.data:
            print '%s' % ''.join(r)
            fout.write('\n%s' % ''.join(r))

    def solve(self):
        fin = open('../in.in', 'r')
#         fin = open('../test', 'r')
#         fin = open('../example.txt', 'r')
        fout = open('../out', 'w')
        times = int(fin.readline())
        for i in range(times):
            fout.write("Case #%d: " % (i + 1))
            print "Case #%d: " % (i + 1)
            self.process(fin, fout)
            fout.write("\n")
        fin.close()
        fout.close()
        print 'Done!'

    def make_test(self):
        fout = open('../test', 'w')
        for i in range(25):
            fout.write('A')
            for j in range(24):
                fout.write('?')
            fout.write('\n')
        fout.close()


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
    t.solve()
