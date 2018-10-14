from sys import stdin, stdout
from string import rstrip
from operator import xor

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))

line = 0
testcase = 1
while True:
    tokens = input[line].split(' ')
    N = int(tokens[0])
    M = int(tokens[1])
    line+=1
    D = input[line:line+N]
    line+=N
    L = input[line:line+M]
    line+=M
    stdout.write("Case #%s: "%testcase)
    testcase+=1
    for order in L:
        maxpenalties = -1
        order = list(order)
        for word in D:
            nchars = len(word)
            npenalties = 0
            P = D
            word = list(word)
            for letter in order:
                P = [p for p in P if p and len(p) == nchars]
                valid = False
                for p in P:
                    if letter in p: valid = True
                if not valid: continue
                if letter not in word: npenalties += 1
                for pindex, p in enumerate(P):
                    p = list(p)
                    for lindex, l in enumerate(p):
                        if word[lindex] == letter and l != letter: P[pindex]=0
                        if word[lindex] != letter and l == letter: P[pindex]=0
            if npenalties > maxpenalties:
                maxpenalties = npenalties
                bestpenalty = ''.join(word)
        stdout.write(bestpenalty+' ')

    stdout.write('\n')
    if testcase > nTestCases: break


