#!/usr/bin/python
src = open("A-large.in")
content = src.read().split("\n")
(L,D,N) = content[0].split(" ")

L = int(L)
D = int(D)
N = int(N)

wordList = content[1:D+1]
pattList = content[D+1:D+N+1]

def makePattern(patt):
    pattern = []
    while len(patt) > 0:
        if patt[0] != '(':
            pattern.append([patt[0]])
            patt = patt[1:]
        else:
            end = patt.index(')')
            pattern.append(list(patt[1:end]))
            patt = patt[end+1:]
    return pattern

def match(pattern, word):
    length = len(word)
    for i in range(length):
        if word[i] in pattern[i]:
            continue
        return False
    return True

for case in range(N):
    pattern = makePattern(pattList[case])
    cnt = 0
    for word in wordList:
        if match(pattern, word):
            cnt += 1

    output = "Case #"
    output += str(case+1)
    output += ": "
    output += str(cnt)

    print output

