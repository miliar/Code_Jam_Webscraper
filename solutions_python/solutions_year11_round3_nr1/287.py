#!/usr/bin/env python

infile = "A-large.in"
#infile = "A-small-attempt0.in"
#infile = "A-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    R, C = [int(value) for value in fsrc.readline().split()]
    arr = []
    for i in range(R):
        arr.append(list(fsrc.readline()))

    open = 0
    num = 0
    impossible = False
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '#':
                num += 1
                if r+1 == R or c+1 == C or arr[r+1][c] != '#' or arr[r+1][c+1] != '#' or arr[r][c+1] != '#':
                    impossible = True
                    break
                else:
                    arr[r][c] = '/'
                    arr[r+1][c] = '\\'
                    arr[r+1][c+1] = '/'
                    arr[r][c+1] = '\\'
        if impossible:
            break

    
    res = "Case #%s:\n" %(t+1, ) 
    if impossible:
        res += 'Impossible\n'
    else:
        for value in arr:
            res += ''.join(value) + '\n'
            res = res[:-1]
    print res
    fres.write(res)

fsrc.close()
fres.close()
