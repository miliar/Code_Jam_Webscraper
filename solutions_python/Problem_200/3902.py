import sys
import unittest

def tidy(n):
    return ''.join(sorted(str(n))) == str(n)

def solve(n):
    for i in range(n, 0, -1):
        if tidy(i):
            return i
            break

def new_solve(n):
    s = str(n)
    while not tidy(n):
        for i in range(1, len(s)):
            if s[i] < s[i - 1]:
                n -= int(s[i:]) + 1
                s = str(n)
                break
    return n

class BigTest(unittest.TestCase):
    def test_old_new_same(self):
        for i in range(1, 100000):
            self.assertEqual(solve(i), new_solve(i))

# unittest.main()

if __name__ == '__main__':
    f = sys.stdin
    f.readline()
    case = 1
    for s in f:
        print("Case #{}: {}".format(case, new_solve(int(s))))
        case += 1
