import sys
import collections
sys.setrecursionlimit(10000)

def solve(finName, function, step):
    fin = open(finName, "r")
    fout = open(finName+"out", "w")
    
    lines = fin.readlines()
    case = 1
    for i in range(1, int(lines[0]) * step + 1, step):
        args = [e.rstrip() for e in lines[i : i+step]]
        fout.write("Case #" + str(case) + ": " + function(args) + "\n")
        case += 1
        if case % 10000 == 0: print ("+10000")
    fin.close()
    fout.close()

def deceitfulWar(args):
    nBlocks = int(args[0])
    
    blocksNaomi = []
    blocksKen = []
    for block in args[1].split(" "):
        blocksNaomi.append(float(block))
    for block in args[2].split(" "):
        blocksKen.append(float(block))
    blocksNaomi.sort()
    blocksKen.sort()

    scoreFair = nBlocks
    blocksKenTemp = list(blocksKen)
    for i in range(nBlocks):
        for j in range(len(blocksKenTemp)):
            if blocksKenTemp[j] > blocksNaomi[i]:
                scoreFair-=1
                blocksKenTemp.remove(blocksKenTemp[j])
                break

    blocksNaomi = blocksNaomi[::-1]
    blocksKen = blocksKen[::-1]
    scoreCheat = nBlocks
    for i in range(nBlocks):
        if blocksKen[0] > blocksNaomi[0]:
            scoreCheat-=1
            blocksNaomi.pop()
        else:
            blocksNaomi.pop(0)
        blocksKen.pop(0)
    return str(scoreCheat) + " " + str(scoreFair)

if __name__=="__main__":
    solve("D-large.in", deceitfulWar, 3)
    print("done")
