##
# CODEJAM
# prillan91
##
import sys


def solveSingle(f):
    [R, C] = f.readline().split(' ')
    (R, C) = (int(R), int(C))
    
    pic = []

    def printPic():
        ret = ""
        for r in range(R):
            ret += "\n" + ''.join(pic[r])
        return ret

    for i in range(R):
        pic.append(list(f.readline().strip()))
        
    #print printPic()

    def editSquare(i, j, s):
        #print (i, j, s)
        if i < len(pic) and j < len(pic[i]) and pic[i][j] == '#':
            pic[i][j] = s
            return True
        return False
    for r in range(R):
        for c in range(C):
            if pic[r][c] == '#':
                #print (r, c, "/")
                #BEGIN BLOCK
                pic[r][c] = "/"
                if not (editSquare(r+1, c, "\\") and editSquare(r, c + 1, "\\") and editSquare(r + 1, c + 1, "/")):
                    return "\nImpossible"
                last = '\\'
            
    

    return printPic()
def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)) + "\n")
        


solve()
