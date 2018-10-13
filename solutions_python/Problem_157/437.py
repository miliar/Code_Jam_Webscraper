# coding=utf-8
import unittest

filename = "C-small-attempt0"
format = "Case #%d: %s\n"

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.input = open(filename + ".in", 'r')
        self.output = open(filename + ".out", 'w')
    
    def tearDown(self):
        self.input.close()
        self.output.close()
    
    def testSolve(self):
        answer = ['NO', 'YES']
        multi ={'1':{'1':'1', 'i':'i', 'j': 'j', 'k': 'k'}, 
                'i':{'1':'i', 'i':'-1', 'j': 'k', 'k': '-j'},
                'j':{'1':'j', 'i':'-k', 'j': '-1', 'k': 'i'},
                'k':{'1':'k', 'i':'j', 'j': '-i', 'k': '-1'}}
        label = 'ijk'
        lines = self.input.readlines()
        n = int(lines[0].strip())
        lines = lines[1:]
        for i in range(1, n+1):
            (L, X) = map(int, lines[0].strip().split(' '))
            S = lines[1].strip()
            stack = []
            sign = 1
            index = 0
            result = 0
            stack.append('1')
            for j in range(X):
                for k in range(L):
                    if index < 3 and stack[-1] == label[index]:
                        stack.append('1')
                        index += 1
                    if S[k] == '-':
                        sign = -sign
                        k += 1
                    top = stack[-1]
                    stack = stack[:-1]
                    res = multi[top][S[k]]
                    if '-' in res:
                        sign = -sign
                        res = res.replace('-','')
                    stack.append(res)
            if (''.join(stack) == label or ''.join(stack) == label+'1') and sign == 1:
                result = 1
            self.output.write(format%(i, answer[result]))
            lines = lines[2:]

if __name__ == "__main__":
    unittest.main()