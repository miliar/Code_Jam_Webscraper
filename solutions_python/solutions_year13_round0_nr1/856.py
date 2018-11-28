import sys
import logging
import collections as c
logging.basicConfig(level=logging.INFO)

BOARD_DIM = 4

def d(string):
    logging.debug(string)

def printAnswer(case_num, ans):
    print("Case #%d: %s" % (case_num + 1, ans))

def rotateGrid(grid, sn):
    d("Rotating grid")
    # sn is +1 or -1
    rotgrid = []
    i = 0
    for line in grid:
        line = list(line)
        if sn == 1:
            if i != 0:
                line[-i:] = ['s'] * i
        elif sn == -1:
            if i != 0:
                line[:i] = ['s'] * i
                
        q = c.deque(line)
        q.rotate(sn * i)
        i += 1
        rotgrid.append(list(q))

    d("rotgrid is %s" % str(rotgrid))
    return rotgrid

def checkResult(grid):
    ans = ""

    ans = checkGrid(grid)
    if ans:
        return ans
    ans = checkGrid(rotateGrid(grid, 1))
    if ans:
        return ans
    ans = checkGrid(rotateGrid(grid, -1))
    if ans:
        return ans

    return ans

def checkGrid(grid):
    d("Checking grid")
    ans = ""
    for line in grid:
        if "".join(line) == "XXXX" or "TXXX" == "".join(sorted(line)):
            ans = "X won"
        if "".join(line) == "OOOO" or "OOOT" == "".join(sorted(line)):
            ans = "O won"

    grid_t = list(zip(*grid))
    for line in grid_t:
        if "".join(line) == "XXXX" or "TXXX" == "".join(sorted(line)):
            ans = "X won"
        if "".join(line) == "OOOO" or "OOOT" == "".join(sorted(line)):
            ans = "O won"

    return ans

def main(filename):
    f = open(filename, 'r')
    testcases = int(f.readline().strip())
    for t in range(testcases):
        result = "Draw"
        board = []
        for line in range(BOARD_DIM):
            board.append(f.readline().strip())
        ans = checkResult(board)
        if ans:
            result = ans
        else:
            if '.' in [item for sublist in board for item in sublist]:
                result = "Game has not completed"
            
        printAnswer(t, result)
        f.readline()

if __name__ == "__main__":
    main(sys.argv[1])
