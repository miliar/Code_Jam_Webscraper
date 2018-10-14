
# -*- coding: cp949 -*-

import sys, copy

def read_pattern(str):
    pattern = []
    flag = 0
    for ch in str:
        if(flag):
            if(ch != ')'):
                token = token+ch
            else:
                pattern.append(token)
                flag = 0
        else:
            if(ch == '('):
                token = ''
                flag = 1
            else:
                pattern.append(ch)
    return pattern

def is_right_pattern(p,w):
    for i in range(len(w)):
        if(w[i] not in p[i]):
            return False
    return True

if(len(sys.argv) == 1):
    fin = open("ex1.in", 'r')
    fout = open("ex1.out", 'w')
else:
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')

L,D,N = fin.readline().rstrip('\r\n').split()
L,D,N = int(L), int(D), int(N)
            
words = []
patterns = []

for i in range(D):
    words.append(fin.readline().rstrip('\r\n'))
for i in range(N):
    pl = fin.readline().rstrip('\r\n')
    patterns.append(read_pattern(pl))

for i in range(N):
    result = 0
    for w in words:
        if(is_right_pattern(patterns[i],w)):
            result = result+1
        
    fout.write("Case #%d: %d\n" % (i+1, result))

fin.close()
fout.close()
