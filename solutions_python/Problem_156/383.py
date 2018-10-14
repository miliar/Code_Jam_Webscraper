# coding=utf-8
import unittest
import string

filename = "B-large"
format = "Case #%d: %d\n"

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.input = open(filename + ".in", 'r')
        self.output = open(filename + ".out", 'w')
    
    def tearDown(self):
        self.input.close()
        self.output.close()
    
    def testSolve(self):
        import heapq
        lines = self.input.readlines()
        n = int(lines[0].strip())
        lines = lines[1:]
        for i in range(1, n+1):
            D = int(lines[0].strip())
            P = map(int, lines[1].strip().split(' '))
            result = max(P)
            big = result
            for j in range(1, big+1):
                sum = j
                for k in range(D):
                    if P[k]>j:
                        if P[k]%j == 0:
                            sum += (P[k]/j-1)
                        else:
                            sum += (P[k]/j)
                result = min(result, sum)
            self.output.write(format%(i, result))
            lines = lines[2:]

if __name__ == "__main__":
    unittest.main()