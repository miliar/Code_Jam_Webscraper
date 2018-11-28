#!/usr/bin/env python
import sys

case_num = 1
def printres(result):
    global case_num
    print "Case #%s: %s" % (case_num, result)
    case_num += 1

def readline(): 
    return sys.stdin.readline().rstrip('\n')
def splitline(f):
    return map(f, readline().split())

def impossible(row, col, t, R, C):
    if t[row][col] == '.':
        return False
    
    for i in range(C):
        if t[row][i] != '.' and i != col:
            return False

    for i in range(R):
        if t[i][col] != '.' and i != row:
            return False

    return True

def solve():
    R, C = splitline(int)
    t = []
    for i in range(R):
        t.append(list(splitline(str)[0]))

    for i in range(R):
        for j in range(C):
            if impossible(i, j, t, R, C):
                printres("IMPOSSIBLE")
                return

    changes = 0
    for i in range(R):
        row = t[i]
        for j in range(C):
            if row[j] == '<':
                changes += 1
                break
            elif row[j] != '.':
                break

    for i in range(R):
        row = t[i]
        row.reverse()
        for j in range(C):
            if row[j] == '>':
                changes += 1
                break
            elif row[j] != '.':
                break

    for i in range(C):
        col = [x[i] for x in t]
        for j in range(R):
            if col[j] == '^':
                changes += 1
                break
            elif col[j] != '.':
                break

    for i in range(C):
        col = [x[i] for x in t]
        col.reverse()
        for j in range(R):
            if col[j] == 'v':
                changes += 1
                break
            elif col[j] != '.':
                break

    printres(changes)

def main():
    for i in range(int(readline())): solve()

if __name__ == '__main__': 
    main()

