'''
Created on 13 mars 2013

@author: Steeve
'''

import sys

def replace(lawn, new):
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            if (lawn[i][j] == -1):
                lawn[i][j] = new 

def getCol(lawn , j):
    out = []
    for i in range(len(lawn)):
        out.append(lawn[i][j])
    return out

def remaining(lawn, k):
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            if lawn[i][j] == k:
                return True
    return False

def uncut(lawn, h):
    for i in range(len(lawn)):
        if lawn[i].count(-1) + lawn[i].count(h) == len(lawn[i]):
            lawn[i] = [-1] * len(lawn[i])
    for j in range(len(lawn[0])):
        col = getCol(lawn,j)
        if col.count(-1) + col.count(h) == len(col):
            for i in range(len(lawn)):
                lawn[i][j] = -1
            
out_arr = []
filename = sys.argv[1]
with open(filename) as ifi:
    t = int(ifi.readline())
    for i in range(t):
        n , m = [int(num) for num in ifi.readline()[:-1].split(" ")]
        lawn = []
        heightList = []
        for j in range(n):
            line = [int(num) for num in ifi.readline()[:-1].split(" ")]
            lawn.append(line)
            heightList.extend(line)
        heights = sorted(set(heightList))
        answer = "YES"
        for k in heights:
            replace(lawn, k)
            uncut(lawn, k)
            if remaining(lawn, k):
                answer = "NO"
                break
        out_arr.append("Case #" + str(i + 1) + ": " + str(answer) + "\n")
ofilename = filename.split(".")[0] + ".out"
of = open(ofilename, "w")
of.writelines(out_arr)