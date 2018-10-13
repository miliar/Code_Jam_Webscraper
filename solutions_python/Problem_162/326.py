# coding=utf-8
import unittest
from Solution import *

filename = "A-small-attempt3"
format = "Case #%d: %d\n"

class TestSolution(unittest.TestCase):
    def setUp(self):
        """
        self.solution = RoundB1Solution1()
        self.solution.setup(filename)
        """
        self.fin = open(filename + ".in", 'r')
        self.fout = open(filename + ".out", 'w')
    
    def testSolve(self):
        lines = self.fin.readlines()
        n = int(lines[0].strip())
        lines = lines[1:]
        map = {}
        for i in range(1, 21):
            map[i] = i
        for i in range(21, 1000001):
            rev = self.reverse(i)
            if rev < i:
                map[i] = min(map[i-1],map[rev])+1
            else:
                map[i] = map[i-1]+1
        for case in range(1, n+1):
            number = int(lines[case-1])
            res = map[number]
            self.fout.write(format%(case, res))
    
    def reverse(self, number):
        if number < 10:
            return number
        ret = number % 10
        if ret != 0:
            number /= 10
            while number != 0:
                ret *= 10
                ret += number % 10
                number /= 10
        else:
            ret = number
        return ret
    
    def tearDown(self):
        self.fin.close()
        self.fout.close()

if __name__ == "__main__":
    unittest.main()