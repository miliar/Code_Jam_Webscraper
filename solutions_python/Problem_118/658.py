'''
Created on 13 Apr 2013

@author: mengda
'''
import math

def isP(num):
    num = str(int(num))
    for i in range(len(num) / 2):
        if num[i] <> num[-1 - i]:
            return False
    return True

def createP(root, half_digits, ls):
    root = str(root)
    for i in range(half_digits):
        ls[i] = root[i]
        ls[-1 - i] = root[i]
    return int(''.join(ls))

def process(A, B):
    rlt = 0
    a = int(math.ceil(math.sqrt(A)))
    b = int(math.floor(math.sqrt(B)))
    str_a = str(a)
    half_digits = int(math.ceil(len(str_a) / 2.0))
    root = int(str_a[:half_digits])
    next_root = 10 ** half_digits
    digits = len(str_a)
    ls = []
    for _ in range(digits - len(ls)):
        ls.append('')
    while True:
        if root == next_root:
            if digits % 2 == 0:
                next_root *= 10
                half_digits += 1
            else:
                root /= 10
            digits += 1
            ls.append('')
        p = createP(root, half_digits, ls)
        if p < a:
            root += 1
            continue
        if p > b:
            break
        if isP(math.pow(p, 2)):
            rlt += 1
        root += 1
    return rlt

def process1(A, B):
    rlt = 0
    a = int(math.ceil(math.sqrt(A)))
    b = int(math.floor(math.sqrt(B)))
    for i in range(a, b + 1):
        if not isP(i):
            continue
        power = math.pow(i, 2)
        if isP(power):
            print i
            rlt += 1
    return rlt

f = open('C-large-1.in', 'r')
T = int(f.readline())
outLine = []

for i in range(1, T + 1):
    (A, B) = map(int, f.readline().split())
    outLine.append('Case #%d: %s\n' % (i, process(A, B)))
    print outLine[-1],

f.close()
outFile = open('C-L1.out', 'w')
outFile.writelines(outLine)
outFile.close()
