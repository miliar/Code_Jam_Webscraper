#!/usr/bin/env python

def changeState(state):
    #state
    #toggle all powered on Snapper
    i=0
    while i<len(state) and state[i]==1:
        state[i]=0
        i+=1
    if i<len(state):
        if state[i]==1: state[i]=0
        else: state[i]=1
    return state

def checkState(state):
    for i in state:
        if i==0: return False
    else: return True

ouf = open("output.txt",'w')
with open("input.txt",'r') as inf:
    numOfTest = int(inf.readline()[:-1])
    for i in range(numOfTest):
        test = inf.readline()[:-1].split(' ')
        n = int(test[0])
        k = int(test[1])
        state = [0 for l in range(n)]
        for j in range(k):
            state = changeState(state)
        ouf.write('Case #%s: %s\n'%(i+1,'ON' if checkState(state) else 'OFF'))

ouf.close()
