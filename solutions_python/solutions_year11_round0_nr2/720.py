'''
Created on May 7, 2011

@author: dan
'''

def isIn(ch, str):
    for chInStr in str:
        if ch == chInStr:
            return True
    return False


def combines(evaluation, combination):
    length = len(evaluation)
    if (length < 2):
        return -1
    for index in range(len(combination)):
        word = combination[index]
        if (evaluation[length-1]==word[0]) and (evaluation[length-2]==word[1]):
            return index
        elif evaluation[length-1]==word[1] and evaluation[length-2]==word[0]:
            return index
    return -1

def opposes(evaluation, opposed):
    length = len(evaluation)
    if length<2:
        return False
    ch1 = evaluation[length-1]
    for ch2 in evaluation[0:length-1]:
        for word in opposed:
            if word[0]==ch1 and word[1]==ch2:
                return True
            elif word[0]==ch2 and word[1]==ch1:
                return True
    return False

def eval(ln):
    a = ln.split()
    c = int(a.pop(0))
    combine = []
    for word in a[0:c]:
        combine.append(word)
        a.pop(0)
    n = int(a.pop(0))
    opposed = []
    for word in a[0:n]:
        opposed.append(word)
        a.pop(0)
    a.pop(0)
    element = a.pop(0)
    evaluation = ""
    for ch in element:
        evaluation=evaluation+ch
        cRes = combines(evaluation, combine)
        if (cRes != -1):
            evaluation = evaluation[0:len(evaluation)-2]+combine[cRes][2]
        elif opposes(evaluation, opposed):
            evaluation = ""
    if (len(evaluation)==0):
        return evaluation
    e2=evaluation[0]
    for ch in evaluation[1:]:
        e2 = e2 + ", " + ch
    return e2

import sys
if (len(sys.argv) >1) :
    fname = sys.argv[1]
else:
    fname = "../input.txt"
f = open(fname)
for j in range(int(f.readline())):
    line = f.readline()
    print "Case #"+str(j+1)+": [" + eval(line) + "]"