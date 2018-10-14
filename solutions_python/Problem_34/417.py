#!/usr/bin/python
#Alien Language
import sys
words = []
validAt = []
L = 0
D = 0
N = 0
inputStage = 0
acc = 0

def tokenize(string):
    ret = []
    at = 0
    for i in range(0,L):
        front = string.find('(',at)
        if front != at:
            ret.append([string[at]])
            at += 1
            continue
        back = string.find(')',at)
        tmp = []
        for j in string[front+1:back]:
            tmp.append(j)
        ret.append(tmp)
        at = back + 1
    return ret
    
def canMatch(tokens, word):
    acc = 0
    for char in word:
        if not char in tokens[acc]:
            return False
        acc += 1
    return True
        
def solve(case):
    tokens = tokenize(case)
    #Tokens MUST be L long
    ans = 0
    for word in words:
        if canMatch(tokens, word):
            ans += 1
    return ans
#Had a generate and filter, should have realized that was too slow
#return len(filter(lambda s: s in words, tmp))
        
#Main
for line in sys.stdin.readlines():
    if(inputStage == 0):
        line2 = line.split(' ');
        L = int(line2[0])
        D = int(line2[1])
        P = int(line2[2])
        for i in range(0, L):
            validAt.append(set())
        inputStage = 1
        acc = D
        continue
    elif(inputStage == 1):
        words.append(line.rstrip());
        for i in range(0, L):
            validAt[i].add(line[i])
        acc -= 1
        if(acc == 0):
            inputStage = 2
            acc = 0
    else: #input stage 3
        acc += 1
        print('Case #'+str(acc)+": " + str(solve(line.rstrip())))
