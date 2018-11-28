import sys


def solution(inFile):
    R, C, M = inFile.readline().split(" ")
    R, C, M = int(R), int(C), int(M)
    
    grid = []
    for i in xrange(R):
        grid.append([])
        for j in xrange(C):
            grid[i].append(".")
    
    right = True
    r = ""
    x = 0
    y = 0
    _x = 1
    _y = 0
    i = 0
    if R == 1 or C == 1:
        if R * C - 1 >= M:
            while i < M:
                if grid[x][y] != "*":
                    grid[x][y] = "*"
                    i += 1
                if right:
                    y += 1
                    if y == C:
                        right = False
                        y = _y
                        _y += 1
                else:
                    x += 1
                    if x == R:
                        right = True
                        x = _x
                        _x += 1
            grid[R - 1][C - 1] = "c"
            for elem in grid:
                r += "".join(elem) + "\n"
            return r
        else:
            return "Impossible\n"

    elif R == 2 or C == 2:
        if R * C - M == 1:
            if R < C:
                right = False
            while i < M:
                if grid[x][y] != "*":
                    grid[x][y] = "*"
                    i += 1
                if right:
                    y += 1
                    if y == C:
                        y = 0
                        x += 1
                else:
                    x += 1
                    if x == R:
                        x = 0
                        y += 1
            grid[R - 1][C - 1] = "c"
            for elem in grid:
                r += "".join(elem) + "\n"
            return r              
        elif M % 2 == 0:
            if R * C - 4 >= M:
                if R < C:
                    right = False
                while i < M:
                    if grid[x][y] != "*":
                        grid[x][y] = "*"
                        i += 1
                    if right:
                        y += 1
                        if y == C:
                            y = 0
                            x += 1
                    else:
                        x += 1
                        if x == R:
                            x = 0
                            y += 1
            else:
                return "Impossible\n"
            grid[R - 1][C - 1] = "c"
            for elem in grid:
                r += "".join(elem) + "\n"
            return r
        else:
            return "Impossible\n"

    else:
        size = R * C
        if M in [size, size - 2, size - 3, size - 5, size -7]:
            return "Impossible\n"
        elif M > size:
            return "Impossible\n"
        else:
            if R < C:
                right = False
                _x = 0
                _y = 1
            if R == 3 and C == 4 and M == 2:
                right = True
                _x = 1
                _y = 0
            elif R == 3 and C == 5 and M == 2:
                right = True
                _x = 1
                _y = 0
            elif R == 3 and C == 5 and M == 6:
                return "**...\n**...\n**..c\n"
            elif R == 3 and C == 5 and M == 11:
                return "*****\n***..\n***.c\n"
            elif R == 4 and C == 3 and M == 2:
                right = False
                _x = 1
                _y = 0
            elif R == 4 and C == 4 and M == 3:
                return "**..\n*...\n....\n...c\n"
            elif R == 4 and C == 4 and M == 6:
                return "****\n**..\n....\n...c\n"
            elif R == 4 and C == 5 and M == 3:
                right = True
                _x = 1
                _y = 0
            elif R == 4 and C == 5 and M == 7:
                return "*****\n**...\n.....\n....c\n"
            elif R == 4 and C == 5 and M == 10:
                return "*****\n***..\n*....\n*...c\n"
            elif R == 5 and C == 3 and M == 2:
                return "*..\n*..\n...\n...\n..c\n"
            elif R == 5 and C == 3 and M == 6:
                return "***\n***\n...\n...\n..c\n"
            elif R == 5 and C == 3 and M == 11:
                return "***\n***\n***\n*..\n*.c\n"
            elif R == 5 and C == 4 and M == 3:
                return "**..\n*...\n....\n....\n...c\n"
            elif R == 5 and C == 4 and M == 7:
                return "****\n**..\n*...\n....\n...c\n"
            elif R == 5 and C == 4 and M == 10:
                return "****\n****\n**..\n....\n...c\n"
            elif R == 5 and C == 5 and M == 4:
                return "**...\n**...\n.....\n.....\n....c\n"
            elif R == 5 and C == 5 and M == 8:
                return "*****\n***..\n.....\n.....\n....c\n"
            elif R == 5 and C == 5 and M == 12:
                return "*****\n*****\n**...\n.....\n....c\n"
            elif R == 5 and C == 5 and M == 15:
                return "*****\n*****\n*****\n.....\n....c\n"

            while i < M:
                if grid[x][y] != "*":
                    grid[x][y] = "*"
                    i += 1
                if right:
                    y += 1
                    if y == C:
                        right = False
                        y = _y
                        _y += 1
                else:
                    x += 1
                    if x == R:
                        right = True
                        x = _x
                        _x += 1 
            grid[R - 1][C - 1] = "c"
            for elem in grid:
                r += "".join(elem) + "\n"
            # print r
            return r

inFile = open(sys.argv[1], "r")
outFile = open("out", "w")

N = int(inFile.readline())
for i in range(N):
    outFile.write("Case #%d: \n" % (i + 1))
    outFile.write(str(solution(inFile)))

inFile.close()
outFile.close()
