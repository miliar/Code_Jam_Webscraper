from sys import stdin, stdout


def solve(R, C, mat):
    """
    . period = no arrow
    ^ caret = up arrow
    > greater than = right arrow
    v lowercase v = down arrow
    < less than = left arrow
    """
    rowTally = [0]*R
    colTally = [0]*C
    for r in range(R):
        for c in range(C):
            if mat[r][c] != ".":
                rowTally[r] += 1
                colTally[c] += 1


    change = 0
    
    for r in range(R):
        for c in range(C):
            
            # yes i have heard of functions
            if mat[r][c] == "v":
                if not any( mat[r_][c] != "." for r_ in range(r+1,R) ):
                    if rowTally[r] > 1 or colTally[c] > 1:
                        change += 1
                    else:
                        return "IMPOSSIBLE"

            elif mat[r][c] == "^":
                if not any( mat[r_][c] != "." for r_ in range(0,r) ):
                    if rowTally[r] > 1 or colTally[c] > 1:
                        change += 1
                    else:
                        return "IMPOSSIBLE"


            elif mat[r][c] == ">":
                if not any( mat[r][c_] != "." for c_ in range(c+1,C) ):
                    if rowTally[r] > 1 or colTally[c] > 1:
                        change += 1
                    else:
                        return "IMPOSSIBLE"

            elif mat[r][c] == "<":
                if not any( mat[r][c_] != "." for c_ in range(0,c) ):
                    if rowTally[r] > 1 or colTally[c] > 1:
                        change += 1
                    else:
                        return "IMPOSSIBLE"

    return change



if __name__ == '__main__':

    T = int(stdin.readline())

    for i in range(T):
        # read input for this problem

        R, C = map(int, stdin.readline().strip().split())
        mat = []
        for j in range(R):
            mat.append(stdin.readline().strip())

        result = solve(R, C, mat)

        print "Case #%d: %s"%(i+1, result)