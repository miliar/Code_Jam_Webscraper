

def first_minus(x, index):
    for i, c in enumerate(x[index:]):
        if c == '-':
            return i
    return len(x)


if __name__ == '__main__':
    import sys
    n = int(sys.stdin.readline())

    for case in range(1, n + 1):
        line = sys.stdin.readline()
        s, k = line.split()
        s = list(s)
        k = int(k)

        swaps = 0
        for i in range(len(s) - k + 1):
            if s[i] == '-':
                swaps += 1
                for j in range(i, i+k):
                    s[j] = '+' if s[j] == '-' else '-'

        print_res = lambda res: print('Case #%d: %s' % (case, res))
        if all([c == '+' for c in s[-k:]]):
            print_res(swaps) 
        else:
            print_res('IMPOSSIBLE') 



import unittest

class Test(unittest.TestCase):
    def test_first_minus(self):
        l = [
                ('++-', 2),
                ('---', 0),
                ('+++', 3),
                ]
        for s, i in l:
            self.assertEqual(i, first_minus(s, 0))
