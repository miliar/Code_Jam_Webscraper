from __future__ import print_function


class Template:
    def __init__(self):
        self.cout = False

    def process(self):
        self.ans = []
        self.tmp_pos = []
        self.N, self.R, self.O, self.Y, self.G, self.B, self.V = [
            int(x) for x in self.fin.readline().strip().split()]
#         self.print_tmp('%s, %s, %s, %s, %s, %s, %s' % (N, R, O, Y, G, B, V))
        todo = reversed(sorted([self.B, self.Y, self.R]))
        for x in todo:
            self.do(x)
#         self.put_r()
#         self.put_y()
#         self.put_b()

        self.cal_same()
        if len(self.tmp_pos) > 0:
            print(''.join(self.ans))
            self.ans = 'IMPOSSIBLE'
        self.print_ans(''.join(self.ans))

    def check_last(self):
        if self.ans[-1] == self.ans[0]:
            return True
        return False

    def do(self, x):
        if self.R == x:
            self.put_c('R', self.R)
            self.R = 0
        elif self.Y == x:
            self.put_c('Y', self.Y)
            self.Y = 0
        elif self.B == x:
            self.put_c('B', self.B)
            self.B = 0

    def put_c(self, c, count):
        tmp = count
        self.cal_same()
        for x in self.tmp_pos:
            if tmp:
                tmp = tmp - 1
                self.ans.insert(x, c)
        if tmp:
            self.insert(c, tmp)

    def insert(self, c, count):
        todo = count
        for x in range(len(self.ans) - 1):
            if (self.ans[x] != c) and (self.ans[x + 1] != c):
                if todo > 0:
                    todo = todo - 1
                    self.ans.insert(x + 1, c)
                else:
                    break
        if self.ans and (self.ans[0] != c) and (self.ans[-1] != c):
            if todo > 0:
                todo = todo - 1
                self.ans.append(c)
        for _ in range(todo):
            self.ans.append(c)

    def cal_same(self):
        self.tmp_pos = []
        for x in range(len(self.ans) - 1):
            if self.ans[x] == self.ans[x + 1]:
                self.tmp_pos.insert(0, x + 1)
        if self.ans and self.ans[0] == self.ans[-1]:
            self.tmp_pos.insert(0, len(self.ans))

    def solve(self):
        self.fin = open('../in.in', 'r')
        # fin = open('../test', 'r')
#         self.fin = open('../example.txt', 'r')
        self.fout = open('../out', 'w')
        times = int(self.fin.readline())
        for i in range(times):
            self.print_ans('Case #%d: ' % (i + 1))
            self.process()
            self.print_ans('\n')
        self.fin.close()
        self.fout.close()
        print('Done!')

    def make_test(self):
        fout = open('../test', 'w')
        fout.write('1\n2000\n')
        for i in range(2000):
            fout.write('%d %d\n' % ((-1000 + i), 1000 - i))
        fout.close()

    def print_tmp(self, s):
        if self.cout:
            print(str(s))

    def print_ans(self, s):
        self.fout.write(str(s))
        if self.cout:
            print(str(s), end='')


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
    t.solve()
