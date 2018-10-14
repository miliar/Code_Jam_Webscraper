# coding=utf-8
import unittest
import string

filename = "A-large"
format = "Case #%d: %d\n"

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.input = open(filename + ".in", 'r')
        self.output = open(filename + ".out", 'w')
    
    def tearDown(self):
        self.input.close()
        self.output.close()
    
    def testSolve(self):
        lines = self.input.readlines()
        n = int(lines[0].strip())
        lines = lines[1:]
        for i in range(1, n+1):
            (length, s) = lines[0].strip().split(' ')
            length = int(length)
            sum = 0
            stand = int(s[0])
            if length!=0:
                for j in range(1, length+1):
                    incre = 0
                    if int(s[j]) == 0:
                        continue
                    elif j>stand:
                        incre = j-stand
                        sum += incre
                    stand = stand + incre + int(s[j])
            self.output.write(format%(i, sum))
            lines = lines[1:]

if __name__ == "__main__":
    unittest.main()