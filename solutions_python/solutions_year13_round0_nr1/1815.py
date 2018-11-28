import os

class TicTacToe(object):
    def __init__(self):
        self.table = []

    def appendRow(self, str):
        arr = []
        for ch in str:
            arr.append(ch)
        self.table.append(arr)

    # w: X or O
    def check_if_winner(self, w):
        # check columns if 4 X's
        for i in xrange(0, 4):
            found = True
            for j in xrange(0,4):
                if (self.table[i][j] != w and self.table[i][j] != 'T'):
                    found = False
                    break
            if (found):
                return True
        # check rows if 4 X's
        for i in xrange(0, 4):
            found = True
            for j in xrange(0,4):
                if (self.table[j][i] != w and self.table[j][i] != 'T'):
                    found = False
                    break
            if (found):
                return True
        # check diag if 4 X's
        found = True
        for i in xrange(0,4):
            if (self.table[i][i] != w and self.table[i][i] != 'T'):
                found = False
                break
        if (found):
            return True
        found = True
        for i in xrange(0,4):
            if (self.table[i][3-i] != w and self.table[i][3-i] != 'T'):
                found = False
                break
        if (found):
            return True
        return False

    def check_if_not_finished(self):
        for i in xrange(0,4):
            for j in xrange(0,4):
                if (self.table[i][j] == '.'):
                    return True
        return False


input_file = open(os.getcwd() + "/A.in", 'r')

T = input_file.readline()

for i in xrange(0,int(T)):
    game = TicTacToe()
    for row in xrange(0,4):
        game.appendRow(input_file.readline())
    input_file.readline() # get empty line

    print "Case #%d:" % (i+1),
    # check if X wins
    if (game.check_if_winner('X')):
        print "X won"
    # check if O wins
    elif (game.check_if_winner('O')):
        print "O won"
    # check if game not over
    elif (game.check_if_not_finished()):
        print "Game has not completed"
    # if none of the above, it is a draw
    else:
        print "Draw"
