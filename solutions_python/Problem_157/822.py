#!/usr/bin/python

'''
Google Code Jam 2015
By gweizman@gmail.com
'''
import sys

class Input:
    def __init__(self, base, X):
        self.base = list(base)
        self.X = X
        self._len = len(self.base) * self.X
        
    def len(self):
        return self._len
    
    def __getitem__(self, i):
        return self.base[i % len(self.base)]

class Quaternion:
    # 1 = 1, 2 = i, 3 = j, 4 = k
    table = [
        [(1, False), (2, False), (3, False), (4, False)], 
        [(2, False), (1, True), (4, False), (3, True)], 
        [(3, False), (4, True), (1, True), (2, False)], 
        [(4, False), (3, False), (2, True), (1, True)]
    ]
    
    @staticmethod
    def toNum(letter):
        return {
            '1': 1,
            1: 1,
            'i': 2,
            2: 2,
            'j': 3,
            3: 3,
            'k': 4,
            4: 4
        }[letter]
    
    @staticmethod
    def toLetter(num):
        '''
        Debugging
        '''
        return {
            1: '1',
            2: 'i',
            3: 'j',
            4: 'k'
        }[num]
    
    def __init__(self, type, negative = False):
        self.type = Quaternion.toNum(type)
        self.negative = negative
    
    def right_mul(self, b):
        result = self.table[self.type - 1][Quaternion.toNum(b) - 1]
        return Quaternion(result[0], result[1] != self.negative)
        
    def left_div(self, a):
        num = Quaternion.toNum(a)
        for i in range(0, 4):
            if self.table[num - 1][i][0] == self.type:
                return Quaternion(i + 1, self.table[num - 1][i][1] != self.negative)
        return False
        
    def __str__(self):
        return ("-" if self.negative else "") + Quaternion.toLetter(self.type)

def testcase(input):
    global first_break, second_break, first, second, third
    
    def printState(prefix = ""):
        print prefix, first, second, third
    
    def incFirst():
        global first_break, second_break, first, second, third
        if second_break - first_break <= 1:
            if incSecond() != False:
                return incFirst()
            return False
        first_break += 1
        first = first.right_mul(input[first_break - 1])
        second = second.left_div(input[first_break - 1])
        
    def incSecond():
        global first_break, second_break, first, second, third
        if input.len() - second_break <= 1:
            return False
        second_break += 1
        second = second.right_mul(input[second_break - 1])
        third = third.left_div(input[second_break - 1])
    
    if (input.len() >= 3):
        first_break = 1
        second_break = 2
        first = Quaternion(input[0], False)
        second = Quaternion(input[1], False)
        third = Quaternion(input[2], False)
        i = 3
        while i < input.len():
            third = third.right_mul(input[i])
            i += 1
        if (str(first) == 'i') and (str(second) == 'j') and (str(third) == 'k'):
            return "YES"
        while first_break < input.len() - 2:
            incFirst()
            while str(first) != 'i' and incFirst() != False:
                continue
            if (str(first) == 'i'):
                tempSecond = second
                tempThird = third
                if (str(second) == 'j') and (str(third) == 'k'):
                    return "YES"
                while second_break < input.len() - 1:
                    incSecond()
                    while str(second) != 'j' and incSecond() != False:
                        continue
                    if (str(second) == 'j') and (str(third) == 'k'):
                        return "YES"
                second = tempSecond
                third = tempThird
        if (str(first) == 'i') and (str(second) == 'j') and (str(third) == 'k'):
            return "YES"
    return "NO"
if len(sys.argv) != 3:
    print 'Usage: python dijkstra.py <input> <output>'
    sys.exit(0)
    
f = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'w')

f.readline() # Skip first line
case = 1
for line in f:
    L,X = line.split()
    input = next(f).rstrip()
    o.write("Case #" + str(case) + ": " + testcase(Input(input, int(X))) + "\n")
    case += 1
    
