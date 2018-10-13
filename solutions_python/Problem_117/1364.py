#!/usr/bin/env python

def isFeasible(matrix, row, col, list):
    if row == 1 or col == 1:
        return "YES"
    list.sort()
    for k in range(len(list)-1):

        min = list[k]
        nextMin = list[k+1]
        cache = {}

        for i in range(0,row):
            for j in range(0,col):
                key = "%d,%d" % (i, j)
                # Visited
                if key in cache:
                    continue
                item = matrix[i][j]
                if item == min:
                    keys = []
                    keys.append(key)
                    isRowValid = True
                    isColValid = True
                    for jj in range(0, col):
                        #print matrix[i][jj]
                        if matrix[i][jj] != min:
                            isRowValid = False
                    for ii in range(0, row):
                        #print matrix[ii][j]
                        if matrix[ii][j] != min:
                            isColValid = False

                    condition = isColValid or isRowValid
                    if condition:
                        if isRowValid:
                            for jj in range(0, col):
                                keys.append("%d,%d" % (i, jj))
                        if isColValid:
                            for ii in range(0, row):
                                keys.append("%d,%d" % (ii, j))

                        # Survived, mark as visited
                        for k in keys:
                            cache[k] = 1
                    else:
                        return "NO"

        # Next round, compare bigger value
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == min:
                    matrix[i][j] = nextMin
    return "YES"

f = open("B-large.in")
lines = f.readlines()

num = int(lines[0])

wfile = open("lk", "w")
index = 1
for i in range(num):
    print i
    matrix = []
    row, col = lines[index].strip().split()
    row = int(row)
    col = int(col)
    numSet = []
    for j in range(row):
        ns = lines[index + j + 1].strip().split()
        introw = []
        for k in range(col):
            v = int(ns[k])
            introw.append(v)
            numSet.append(v)
        matrix.append(introw)
    
    wfile.write("Case #%d: %s\n" % (i+1, isFeasible(matrix, row, col, list(set(numSet)))))
    index += row + 1
