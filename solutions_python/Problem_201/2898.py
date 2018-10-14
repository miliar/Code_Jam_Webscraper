#!/usr/bin/python3
#-*- coding: utf-8 -*-

def FindBestStall(stalls):
    goodIndex = []
    maximum = -1
    for i,e in enumerate(stalls):
        # Unpacking Ls/Rs
        state,Ls,Rs = e
        if state:
            continue
        if min(Ls,Rs) > maximum :
            goodIndex = [i]
            maximum = min(Ls,Rs)
        elif min(Ls,Rs) == maximum :
            goodIndex.append(i)
    
    # goodIndex contains indices for which min(Ls,Rs) is maximal
    if len(goodIndex) == 1:
        # Return the single best element
        return goodIndex[0]

    # Discrimines further stalls :
    # We want the stall that maximize max(Ls,Rs)
    # In case of draw, leftmost one
    maximum = -1
    betterIndex = -1
    for i in goodIndex :
        _,Ls,Rs = stalls[i]
        if max(Ls,Rs) > maximum :
            betterIndex = i
            maximum = max(Ls,Rs)

    return betterIndex


def InitStalls (N):
    stalls = []
    for i in range(N):
        # Stalls are represented by 3-tuples busy,Ls,Rs
        stalls.append((False,i,N-i-1))
    return stalls

def OccupyStall (stalls,index):
    _,Ls,Rs = stalls[index]
    stalls[index] = True,Ls,Rs
    ret = []
    for i in range(len(stalls)):
        state,Ls,Rs = stalls[i]
        if i < index:
            Rs = min (Rs,index-i-1)
        elif i > index:
            Ls = min (Ls,i-index-1)
        if i==index:
            state = True
        ret.append ((state,Ls,Rs))
    return ret


if __name__ == "__main__":
    nbExec = int(input())
    for i in range(nbExec):
        inp = input()
        N = int (inp[:inp.find(" ")])
        K = int (inp[inp.find(" "):])
        stalls = InitStalls (N)
        for j in range (K):
            index = FindBestStall(stalls)
            stalls = OccupyStall (stalls, index)
        _,Ls,Rs = stalls[index]
        print ("Case #{}: {} {}".format(i+1,max(Ls,Rs),min(Ls,Rs)))

