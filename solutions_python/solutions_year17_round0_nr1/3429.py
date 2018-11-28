import sys, unittest
from collections import deque

def flip(p, i, k):
    r = ""
    r += p[:i]
    for j in range(k):
        r += '-' if p[i + j] == '+' else '+'
    r += p[i+k:]
    return r

class FlipTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(flip("---+-++-", 0, 2), "++-+-++-")
    def test2(self):
        self.assertEqual(flip("---+-++-", 1, 2), "-+++-++-")
    def test3(self):
        self.assertEqual(flip("---+-++-", 6, 2), "---+-+-+")
    def test4(self):
        self.assertEqual(flip("---+-++-", 1, 1), "-+-+-++-")
    def test5(self):
        self.assertEqual(flip("---+-++-", 1, 0), "---+-++-")


class Stack:
    def __init__(self, p, f):
        self.p = p
        self.f = f

def solve(p, k):
    s = set()
    q = deque()
    q.append(Stack(p, 0))
    while len(q) > 0:
        p = q.popleft()
        if all(map(lambda c: c == '+', p.p)):
            return str(p.f)
        for i in range(len(p.p) - k + 1):
            f = flip(p.p, i, k)
            if not f in s:
                q.append(Stack(f, p.f + 1))
                s.add(f)

    return "IMPOSSIBLE"




class SolveTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve("---", 3), "1")
    def test2(self):
        self.assertEqual(solve("---+-++-", 3), "3")
    def test3(self):
        self.assertEqual(solve("+++++", 4), "0")
    def test4(self):
        self.assertEqual(solve("-+-+-", 4), "IMPOSSIBLE")
    def test5(self):
        self.assertEqual(solve("+", 4), "0")
    def test6(self):
        self.assertEqual(solve("-", 2), "IMPOSSIBLE")
    def test7(self):
        self.assertEqual(solve("+-+-", 2), "2")
    def test8(self):
        self.assertEqual(solve("-+-+-", 2), "IMPOSSIBLE")
    def test9(self):
        self.assertEqual(solve("+-+-+-+-+-", 2), "IMPOSSIBLE")

if __name__ == '__main__':
    f = sys.stdin
    f.readline()
    case = 1
    for s in f:
        i = s.split(" ")
        print("Case #{}: {}".format(case, solve(i[0], int(i[1]))))
        case += 1
    # unittest.main()
