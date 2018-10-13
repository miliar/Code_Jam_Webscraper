

class Template:
    def init(self):
        self.data = ''
        self.fi = 0

    def process(self, fin, fout):
        self.data = fin.readline().strip()
        self._first_invalid()
        if not self._valid():
            ans = self._find()
        else:
            ans = self.data

#         print str(ans)
        fout.write(str(ans))

    def _valid(self):
        return self.fi == len(self.data)

    def _first_invalid(self):
        for index in range(len(self.data) - 1):
            if self.data[index] > self.data[index + 1]:
                if index == 0:
                    self.fi = 0
                    return
                tmp = self.data[index]
                for i in reversed(range(index)):
                    if self.data[i] != tmp:
                        self.fi = i + 1
                        return
                self.fi = 0
                return
        self.fi = len(self.data)

    def _find(self):
        ans = ''
        if self.data[self.fi] != '1':
            ans += self.data[0:self.fi]
            ans += str(int(self.data[self.fi]) - 1)
        else:
            for _ in range(self.fi):
                ans += '9'
        for _ in range(len(self.data) - self.fi - 1):
            ans += '9'
        return str(int(ans))

    def _last_one(self):
        for x in range(self.fi, len(self.data)):
            if self.data[x] != 1:
                return x - 1
        return len(self.data)

    def solve(self):
        fin = open('../in.in', 'r')
#         fin = open('../test', 'r')
#         fin = open('../example.txt', 'r')
        fout = open('../out', 'w')
        times = int(fin.readline())
        for i in range(times):
            fout.write("Case #%d: " % (i + 1))
            self.process(fin, fout)
            fout.write("\n")
        print 'Done'
        fin.close()
        fout.close()

    def make_test(self):
        fout = open('../test', 'w')
        fout.write('10\n')
        for i in range(1, 11):
            fout.write('%d\n' % i)
        fout.close()


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
#     t.make_test()
    t.solve()
