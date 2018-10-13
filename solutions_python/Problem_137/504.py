from __future__ import print_function
import copy
import sys


def outputField(file, field):
    for i in field:
        for j in i:
            file.write(j)
        file.write("\n")

def outputFieldCon(field):
    for i in field:
        for j in i:
            print(j, end='')
        print("")

def expandEx(field, pos, l):
    if (field[pos[0]][pos[1]] == '*'):
        field[pos[0]][pos[1]] = '.'
        l.append(pos)


def expand(field, pos):
    r = len(field)
    c = len(field[0])
    l = []
    if (pos[0]-1 >= 0):
        if (pos[1]-1 >= 0):
            expandEx(field, (pos[0]-1,pos[1]-1), l)
        if (pos[1] >= 0):
            expandEx(field, (pos[0]-1,pos[1]), l)
        if (pos[1]+1 < c):
            expandEx(field, (pos[0]-1,pos[1]+1), l)
    if (pos[0] >= 0):
        if (pos[1]-1 >= 0):
            expandEx(field, (pos[0],pos[1]-1), l)
        if (pos[1] >= 0):
            expandEx(field, (pos[0],pos[1]), l)
        if (pos[1]+1 < c):
            expandEx(field, (pos[0],pos[1]+1), l)
    if (pos[0]+1 < r):
        if (pos[1]-1 >= 0):
            expandEx(field, (pos[0]+1,pos[1]-1), l)
        if (pos[1] >= 0):
            expandEx(field, (pos[0]+1,pos[1]), l)
        if (pos[1]+1 < c):
            expandEx(field, (pos[0]+1,pos[1]+1), l)

    return [l, field]

def copyField(field):
    f = []
    R = len(field)
    C = len(field[0])
    for j in range(0, R):
        f.append([])
        for k in range(0, C):
            f[j].append(field[j][i])

def rec(field, pos, safePosToAdd):
    if (pos == None):
        return None
    for c in pos: #For all possible expandable dots
        [l, fields] = expand(copy.deepcopy(field), c)
        pos.remove(c)
        if (len(l) == safePosToAdd):
            return fields
        elif (len(l) > safePosToAdd):
            return None
        p = copy.deepcopy(pos)
        for l1 in l:
            p.append(l1)
        res = rec(copy.deepcopy(fields), p, safePosToAdd - len(l))
        if (res != None):
            return res
    return None
        
        
    
sys.setrecursionlimit(100000)
with open("test.txt", "r") as file:
    with open("out.txt", "w") as outFile:
        t = int(file.readline())
        for i in range(1, t+1):

            g = file.readline().rstrip().split(" ")
            R = int(g[0])
            C = int(g[1])
            M = int(g[2])
            
            dots = R*C - M
            field = []
            for j in range(0, R):
                field.append([])
                for k in range(0, C):
                    field[j].append('*')
            if (dots == 1):
                outFile.write("Case #" + str(i) + ":\n")
                field[0][0]='c'
                outputField(outFile, field)
            else:
                pos = [(0,0), (0,1), (1,1)]
                res = None
                outFile.write("Case #" + str(i) + ":\n")
                for c in pos:
                    if (c[0] >= R or c[1] >= C):
                        continue
                    res = rec(copy.deepcopy(field), [c], dots)
                    if (res != None):
                        res[c[0]][c[1]] = 'c'
                        break
                if (res == None):
                    outFile.write("Impossible\n")
                else:
                    outputField(outFile, res)
                print("Done")
