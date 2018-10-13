#!/usr/bin/env python

def check_row(i, vals, n, m):
    row_start = (i//m)*m
    row_end = row_start+m
    row = vals[row_start:row_end]
    target = vals[i]
    for val in row:
        if val > target: return False
    return True

def check_col(i, vals, n, m):
    col = []
    pos = i%m
    while pos < len(vals):
        col.append(vals[pos])
        pos += m
    target = vals[i]
    for val in col:
        if val > target: return False
    return True

def check_square(i, vals, n, m):
    return check_row(i, vals, n, m) or check_col(i, vals, n, m)

def is_possible(vals, n, m):
    for i in range(len(vals)):
        if not check_square(i, vals, n, m):
            return False
    return True

file = open("input.txt")
num_cases = int(file.readline().strip())
for i in range(num_cases):
    n,m = file.readline().split()
    n,m = int(n),int(m)
    vals = []
    for j in range(n):
        vals += file.readline().split()
    vals = list(map(int, vals))
    print("Case #" + str(i+1) + ":", end=" ")
    if is_possible(vals, n, m): print("YES")
    else: print("NO")
file.close()
