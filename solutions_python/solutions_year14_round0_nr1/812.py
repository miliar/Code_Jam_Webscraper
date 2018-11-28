import sys
import collections
sys.setrecursionlimit(10000)

def solve(finName, foutName, function, step):
    fin = open(finName, "r")
    fout = open(foutName, "w")
    
    lines = fin.readlines()
    case = 1
    for i in range(1, int(lines[0]) * step + 1, step):
        args = [e.rstrip() for e in lines[i : i+step]]
        fout.write("Case #" + str(case) + ": " + function(args) + "\n")
        case += 1
        if case % 10000 == 0: print ("+10000")
    fin.close()
    fout.close()
    
def magicTrick(args):
    rowIndex1 = (int)(args[0])
    rowIndex2 = (int)(args[5]) + 5
    row1 = args[rowIndex1].split(" ")
    row2 = args[rowIndex2].split(" ")
    
    matches = 0
    match = ""
    for i in range(4):
        for j in range(4):
            if row1[i] == row2[j]:
                matches+=1
                match = row1[i]
    if matches == 1:
        return match
    if matches == 0:
        return "Volunteer cheated!"
    if matches > 1:
        return "Bad magician!"

if __name__ == "__main__":
    solve("A-small-attempt0.in", "A.txt", magicTrick, 10)
