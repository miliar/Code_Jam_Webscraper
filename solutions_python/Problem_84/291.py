import string
import sys


def check(rows, r,c):
    try:
        return (rows[r][c+1] =="#")and(rows[r+1][c] =="#")and(rows[r+1][c+1] =="#")
    except IndexError:
        return False


f =open(sys.argv[1],"r")
T =int(f.readline())

for i in range (T):
    inp = f.readline().split()
    R = int(inp[0])
    C = int(inp[1])
    rows = []
    flag = True
    for r in range(R):
        rows.append(f.readline().replace("\n",""))#read rows
    for r in range(R):
        for c in range(C):
            if(rows[r][c] == "#"):
                if not (check(rows,r,c)):#check bounds
                    flag = False
                    break
                else:
                    tl = list(rows[r])
                    tl[c] = "/"
                    tl[c+1] = "\\"
                    rows[r] = ''.join(tl)
                    tl = list(rows[r+1])
                    tl[c] = "\\"
                    tl[c+1] = "/"
                    rows[r+1] = ''.join(tl)

        if not (flag):
            break
    print "Case #{0}:".format(i+1)
    if not (flag):
        print "Impossible"
    else:
        for r in range(R):
            print rows[r]
    
