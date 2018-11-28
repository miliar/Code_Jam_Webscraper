#!/usr/bin/python

import sys

def is_valley(rows, r, c, N, M):
    val = rows[r][c]
    up = down = right = left = False
    if r > 0: #CHECK UP
        up = rows[r-1][c] > val
    if r < N - 1: #CHECK DOWN
        down = rows[r+1][c] > val
    if c > 0: #CHECK LEFT
        left = rows[r][c-1] > val
    if c < M - 1: #CHECK RIGHT
        right = rows[r][c+1] > val
    return (up == True or down == True) and (left == True or right == True)

def is_valley_2(rows, r, c, N, M):
    val = rows[r][c]
    vert = True
    horiz = True
    for i in range(0, N):
        if val < rows[i][c]:
            vert = False
            break
    for j in range(0, M):
        if val < rows[r][j]:
            horiz = False
            break
    return vert == False and horiz == False

def can_do_pattern(rows, N, M):
    for r in rows:
        print r
    for r in range(0, len(rows)):
        for c in range(0, len(rows[r])):
            if is_valley_2(rows, r, c, N, M):
                print "No se puede:", r, c, "--", rows[r][c]
                return False
    return True
    

def solve(in_file, out_file):
    cases = int(in_file.readline())
    for case in range(0, cases):
        N, M = [int(x) for x in in_file.readline().split()]
        rows = []
        for row in range(0, N):
             rows.append([int(x) for x in in_file.readline().split()])
        result = can_do_pattern(rows, N, M)
 
        out_file.write("Case #%d: %s\n" % (case+1, "YES" if result else "NO"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print u"Error: Invalid number of arguments. Expected 1 and received %d." % (len(sys.argv) - 1)
        sys.exit(2)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'
    in_file = open(input_file_name, 'r')
    out_file = open(output_file_name, 'w')
    solve(in_file, out_file)
    in_file.close()
    out_file.close()

