import re
import sys

TEXT = "welcome to code jam"
TA = [TEXT[i] for i in range(len(TEXT))]
S = set(TA)

def calc(s):
    str = []

    for i in range(len(s)):
        if s[i] in S:
            str.append(s[i])

    score = [0 for i in range(len(str))]

    total = 1
    for l in TA:
        new = [0 for i in range(len(str))]
        for i in range(len(str)):
            if l == str[i]:
                new[i] = total
            else:
                total += score[i]
        del score
        score = new
        total = 0
    
    return sum(score)



state = 0
Case = 0
#for line in open('A-large.in', 'r'):
#for line in open('C-test', 'r'):
for line in open('C-small-attempt0.in', 'r'):
    if state == 0:
        N = int(line[:-1])
        state = 1
    elif state == 1:
        s = line[:-1]
        Case += 1
        print "Case #"+str(Case)+": "+("0000"+str(calc(s)))[-4::]


