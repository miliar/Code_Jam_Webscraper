def canConvert(M, y, x):
    nx = len(M[0])
    ny = len(M)
    if(x+1 < nx and y+1 < ny):
        if(M[y][x] == "#" and M[y+1][x] == "#" and M[y][x+1] == "#" and M[y+1][x+1] == "#"):
            return True
        else:
            return False
    else:
        return False

def convert(M, x, y):
    M[x][y] = "/"
    M[x][y+1] = "\\"
    M[x+1][y] = "\\"
    M[x+1][y+1] = "/"
    return M

def printM(M):
    for i in M:
        print i
def convertAll(M):
    nx = len(M[0])
    ny = len(M)
    for x in range(nx):
        for y in range(ny):
            if(M[y][x] <> "."):
                if(M[y][x] == "#" ):
                    if(canConvert(M, y, x)):
                        M = convert(M, y, x)
                    else:
                        return "Impossible\n"
    sol = ""
    for i in M:
        for k in i:
            sol = sol + k
        sol = sol + "\n"
    return sol

def solver(name):
    arch = file(name, "r")
    output = file(name + ".out", "w")
    outstr = ""
    T = int(arch.readline())
    lines = arch.readlines()
    pos = 0
    for i in range(T):
        R = int(lines[pos].split()[0])
        C = int(lines[pos].split()[1])
        pos = pos + 1
        M = []
        for j in range(R):
            linea = lines[pos].split()[0]
            row = []
            for k in linea:
                row.append(k)
            M.append(row)
            pos = pos + 1
        outstr = outstr + "Case #" + str(i+1) + ":\n" + convertAll(M)
    output.write(outstr)
    arch.close()
    output.close()
