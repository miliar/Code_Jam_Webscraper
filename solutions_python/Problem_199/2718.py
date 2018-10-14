

class Template:
    def init(self):
        self.s = []
        self.K = 0
        self.c = 0

    def process(self, fin, fout):
        S, K = fin.readline().strip().split()
        self.K = int(K)
        self.s = [x == '+' for x in S]

        self._flip_all()
        ans = self.c if self._check() else 'IMPOSSIBLE'

        print str(ans)
        fout.write(str(ans))

    def _flip_all(self):
        for index in range(len(self.s) + 1 - self.K):
            if not self.s[index]:
                self.c += 1
                self._flip(index)

    def _flip(self, index):
        for i in range(index, index + self.K):
            self.s[i] = not self.s[i]

    def _check(self):
        for x in self.s:
            if not x:
                break
        else:
            return True
        return False

    def solve(self):
        fin = open('../in.txt', 'r')
        # fin = open('../test', 'r')
#         fin = open('../example.txt', 'r')
        fout = open('../out', 'w')
        times = int(fin.readline())
        for i in range(times):
            fout.write("Case #%d: " % (i + 1))
            self.init()
            self.process(fin, fout)
            fout.write("\n")
        fin.close()
        fout.close()

    def make_test(self):
        fout = open('../test', 'w')
        fout.write('1\n2000\n')
        for i in range(2000):
            fout.write('%d %d\n' % ((-1000 + i), 1000 - i))
        fout.close()


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
    t.solve()
