import sys
import unittest

def solve(r, k, n, gs):
    amount = 0
    if n == 1:
        return r * gs[0]
    if k >= sum(gs):
        return r * sum(gs)
    for i in range(r):
        people = 0
        for j in range(n):
            people += gs[j]
            if people > k:
                amount += sum(gs[:j])
                gs = gs[j:] + gs[:j]
                break
    return amount


class SnapperTest(unittest.TestCase):
    def test_solve(self):
        self.assertEquals(21, solve(4, 6, 4, [1, 4, 2, 1]))
        self.assertEquals(100, solve(100, 10, 1, [1]))
        self.assertEquals(20, solve(5, 5, 10, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3]))
        self.assertEquals(13, solve(3, 5, 2, [5, 3]))
        self.assertEquals(18, solve(3, 6, 2, [5, 1]))
        self.assertEquals(50000, solve(1000, 100, 10, [4, 3, 9, 1, 2, 5, 6, 9, 1, 10 ]))

def main(argv):
    if len(argv) == 0: return
    f = open(argv[0], 'r')
    lines = list(f)
    t = int(lines[0])
    for i in range(t):
        r, k, n = (int(x) for x in lines[i * 2 + 1].split(' '))
        gs = [int(x) for x in lines[i * 2 + 2].split(' ')]
        print("Case #%d: %d" % (i + 1, solve(r, k, n, gs))) 
    f.close()

if __name__ == '__main__':
    if sys.argv[1] == 'test':
        unittest.main(argv=('', '-v'))
    else:
        main(sys.argv[1:])
