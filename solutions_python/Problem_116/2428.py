import os

def whowon(matrix):
    dot_exists = 0
    for row in xrange(len(matrix)):        
        xcount = 0
        ocount = 0
        
        # Go through each row and check for a winner
        for column in xrange(len(matrix[row])):
            if matrix[row][column] == 'O':
                ocount += 1
            elif matrix[row][column] == 'X':
                xcount += 1
            elif matrix[row][column] == 'T':
                ocount += 1
                xcount += 1
            else:
                dot_exists = 1
        if xcount == 4:
            return "X won"
        if ocount == 4:
            return "O won"

    # Go through each column and check for a winner
    for column in xrange(len(matrix)):
        xcount = 0
        ocount = 0
        for row in xrange(len(matrix[column])):
            if matrix[row][column] == 'O':
                ocount += 1
            elif matrix[row][column] == 'X':
                xcount += 1
            elif matrix[row][column] == 'T':
                ocount += 1
                xcount += 1
            else:
                dot_exists = 1
        if xcount == 4:
            return "X won"
        if ocount == 4:
            return "O won"
            
    # Go through diagonals and check for a winner
    # Major diagonal
    xcount = 0
    ocount = 0
    for i in xrange(len(matrix)):
        if matrix[i][i] == 'O':
            ocount += 1
        elif matrix[i][i] == 'X':
            xcount += 1
        elif matrix[i][i] == 'T':
            ocount += 1
            xcount += 1
    if xcount == 4:
        return "X won"
    if ocount == 4:
        return "O won"

    # Minor diagonal
    xcount = 0
    ocount = 0
    for i in xrange(len(matrix)):
        if matrix[i][len(matrix)-i-1] == 'O':
            ocount += 1
        elif matrix[i][len(matrix)-i-1] == 'X':
            xcount += 1
        elif matrix[i][len(matrix)-i-1] == 'T':
            ocount += 1
            xcount += 1
    if xcount == 4:
        return "X won"
    if ocount == 4:
        return "O won"
    if dot_exists == 1:
        return "Game has not completed"
    return "Draw"

def makematrix(fd, size):
    t = []
    for i in xrange(size):
        t.append(fd.readline().rstrip('\n'))
    fd.readline() # blank line..
    return t

def solvetictactoe(filename):
    fd = open(filename, "rt")
    out = open("output.txt", "w+t")
    cases = int(fd.readline())
    for i in xrange(cases):
        out.write("Case #" + str(i+1) + ": " + whowon(makematrix(fd, 4)) + "\n")
    fd.close()
    out.close()
    
### MAIN ###

os.chdir("D:/")
solvetictactoe("A-large.in")
