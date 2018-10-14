#!/usr/bin python
import sys

def readline():
    return input.readline().strip(' \r\n\t')

input = sys.stdin

def solve(field,C,R):
    if sum([sum([1 for x in row if x == "#"]) for row in field])%4:
        print "Impossible"
        return
    for c in range(R):
        for r in range(C):
            if field[c][r] == '#':
                #print "found"
                try:
                    if field[c+1][r] == '.' or field[c][r+1] == '.' or field[c+1][r+1] == '.':
                        print "Impossible"
                        return
                    field[c][r] = "/"
                    field[c+1][r] = "\\"
                    field[c][r+1] = "\\"
                    field[c+1][r+1] = "/"
                except IndexError:
                    print "Impossible"
                    return
    for r in range(R):
        print "".join(field[r])
    return

T = int(readline())
for case in range(T):
    print "Case #"+str(case+1)+":"

    tmp = readline().split()
    R = int(tmp[0])
    C = int(tmp[1])
    field = []
    for r in range(R):
        row = readline()
        field.append([c for c in row])
    #print field
    solve(field,C,R)
               
    


