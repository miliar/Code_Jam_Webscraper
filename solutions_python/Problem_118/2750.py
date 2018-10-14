'''
Google Code Jam 

@author: khoipham
'''
from math import sqrt,ceil

def s2ai(s, delimiter = ' '):
    return [int(i) for i in s.strip().split(delimiter)];
    
def array(initVal, cols, rows = 0):
    if rows == 0:
        return [initVal for _ in range(cols) ]
    return [[initVal for _ in range(cols)] for _ in range(rows) ]

def write(s):
    print(s, end='')
    fout.write(s)

def writeln(s):
    print(s)
    fout.write(s + '\n')

def isPLD(num):
    s = str(num)
    l = len(s)
    if l == 1:
        return True
    for i in range(l//2):
        if s[i] != s[l - 1 - i]:
            return False
    return True
    
fin = None
fout = None
if __name__ == '__main__':
    #fin = open('C.in', 'r')
    fin = open('C-small-attempt0.in', 'r')
    #fin = open('C-large.in', 'r')
    fout = open('C.out', 'w')
    
    cases = int(fin.readline())
    for caseIdx in range(1, cases + 1):
        line = fin.readline()
        [A, B] = s2ai(line)
        t = 0
        for i in range(1, ceil(sqrt(B)+1)+1):
            num = i * i
            if num >= A and num <= B and isPLD(num) and isPLD(i):
                t += 1
        
        writeln('Case #%d: %d' % (caseIdx, t ))
        
    fin.close()
    fout.close()
    