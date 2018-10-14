# Python 2.7

def DebugPrint(s, x):
    print "DEBUG(" + s + ") " + str(x)

import sys
import math
import string

def calcLs(k, state):
    for i in reversed(range(0,k)):
        if state[i]:
            return k-i
    DebugPrint("ERROR", [k, s])
    return False

def calcRs(k, state):
    for i in range(k, len(state)):
        if state[i]:
            return i-k
    DebugPrint("ERROR", [k, s])
    return False



def chooseBestStall(oldBest, newCand):
    if oldBest == None:
        return newCand
    elif newCand[1] > oldBest[1]:
        return newCand
    elif newCand[1] == oldBest[1]:
        if newCand[2] > oldBest[2]:
            return newCand
        if newCand[2] == oldBest[2] and newCand[0] < oldBest[0]:
            return newCand
    return oldBest

def calcNextStall(state):
    #ret = []
    bestStall = None
    idx = 0
    for i in range(0,len(state)):
        elm = state[i]
        if elm:
            #DebugPrint("Filled", [i, elm])
            #ret += False
            continue
        Ls = calcLs(i, state)
        Rs = calcRs(i, state)
        #DebugPrint("LsRs", [Ls, Rs])
        minLsRs = min(Ls, Rs)
        maxLsRs = max(Ls, Rs)
        #DebugPrint("MinMaxLsRs", [minLsRs, maxLsRs])
        stall = [i, minLsRs, maxLsRs]
        bestStall = chooseBestStall(bestStall, stall)
        #DebugPrint("beststall", bestStall)
    return bestStall 
        
def solve(N, K):
    State = [True] + [False]*N + [True]
    while K > 0:
        stall = calcNextStall(State)
        #DebugPrint("nextstall", [K, stall])
        State[stall[0]] = True
        K -= 1
        if K == 0:
            return str(stall[2]-1) + " " + str(stall[1]-1)
    return "ERROR"

#DebugPrint("4 2", solve(4,2))
#DebugPrint("5 2", solve(5,2))
#DebugPrint("6 2", solve(6,2))
#DebugPrint("1000 1000", solve(1000,1000))
#DebugPrint("1000 1", solve(1000,1))


def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        N, K = split_input[i+1].split(" ")
        res = solve(int(N), int(K))
        output_file.write("Case #" + str(i+1) + ": " + str(res) + "\n")
    
if __name__ == "__main__":
    main()
