import os

def check_game_state(matrix):
    flag = False
    for row in xrange(4):
        player = matrix[row][0]
        if player == "T":
            player = matrix[row][1]
        if player == ".":
            continue
        flag = True
        for col in xrange(4):
            if matrix[row][col] not in [player, "T"]:
                flag = False
                break
        if flag:
            return player
    #col's
    for col in xrange(4):
        player = matrix[0][col]
        if player == "T":
            player = matrix[1][col]
        if player == ".":
            continue
        flag = True
        for row in xrange(4):
            if matrix[row][col] not in [player, "T"]:
                flag = False
                break
        if flag:
            return player
    #\
    player = matrix[0][0]
    if player == "T":
        player = matrix[1][1]
    if player != ".":
        flag = True
        for i in xrange(4):
            if matrix[i][i] not in [player, "T"]:
                flag = False
                break
    if flag:
        return player
    #/
    
    player = matrix[0][3]
    if player == "T":
        player = matrix[1][2]
    if player != ".":
        flag = True
        for i in xrange(4):
            if matrix[i][3-i] not in [player, "T"]:
                flag = False
                break
    if flag:
        return player
    
    #did gaim end?
    for i in matrix:
        if "." in i:
            return "."
    return "Draw"

def main(args):
    out_string = "Case #%d: %s\n"
    result_string = {"X": "X won",
                     "O": "O won",
                     "Draw": "Draw",
                     ".": "Game has not completed"}
    f = open(args[1])
    out = open(args[2], 'wt')
    number_of_cases = int(f.readline().strip())
    for i in xrange(number_of_cases):
        matrix = [f.readline() for j in xrange(4)]
        f.readline()
        print out_string % (i + 1, result_string[check_game_state(matrix)])
        out.write(out_string % (i + 1, result_string[check_game_state(matrix)]))

if "__main__" == __name__:
    import sys
    import time
    start = time.time()
    main(sys.argv)
    print time.time() - start