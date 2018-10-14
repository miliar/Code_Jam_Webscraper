#!/usr/bin/python

# solution
import sys

class Board(object):
    winner_X = 'X'
    winner_O = '0'
    winner_DRAW = 'Draw'
    winner_INCOMPLETE = 'Incomplete'

    def __init__(self, case_num, string_representation):
        # take in a string that is four characters long and four lines long and store in list of lists
        self.case_num = case_num
        self.string_representation = string_representation
        self.board = string_representation.splitlines()
        #print "\n\n", string_representation, self.board

    def _check_winner(self):
        winner = None

        # check functions return 'X', 'O', check draw returns 'Draw', 'Incomplete'
        if not winner:
            winner = self._check_rows()
            #print 'check rows'

        if not winner:
            winner = self._check_columns()
            #print 'check columns'

        if not winner:
            winner = self._check_diagnals()
            #print 'check diagnals'

        if not winner:
            winner = self._check_draw()
            #print 'check draw'

        self.winner = winner
        #print "Winner: %s\n" % winner

    def _check_draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '.':
                    return self.winner_INCOMPLETE
        return self.winner_DRAW

    def _check_columns(self):
        for i in range(len(self.board)):
            col = [self.board[0][i], self.board[1][i], self.board[2][i], self.board[3][i]]
            result = self._check_list(col)
            if result:
                return result
        return None

    def _check_list(self, list_to_check):
        #print "Checking out", list_to_check
        solution_found = True
        for i in list_to_check:
            if i == 'O' or i == 'T' and solution_found:
                solution_found = True
            elif i == 'X' or i == '.':
                solution_found = False
                break

        if solution_found:
            return self.winner_O

        solution_found = True
        for i in list_to_check:
            if i == 'X' or i == 'T' and solution_found:
                solution_found = True
            elif i == 'O' or i == '.':
                solution_found = False
                break

        if solution_found:
            return self.winner_X

        return None

    def _check_rows(self):
        # make the row into its own list and then _check_list will work

        for i in range(len(self.board[0])):
            row = [self.board[i][0], self.board[i][1], self.board[i][2], self.board[i][3]]

            result = self._check_list(row)
            if result:
                return result
        return None

    def _check_diagnals(self):
        # make the diagnals into thier own list and then _check_list will work
        diag = [self.board[0][0], self.board[1][1], self.board[2][2], self.board[3][3]]
        result = self._check_list(diag)
        if result:
            return result
        else:
            diag = [self.board[3][0], self.board[2][1], self.board[1][2], self.board[0][3]]
            result = self._check_list(diag)
            if result:
                return result


        return None

    def print_result(self):
        self._check_winner()
        if self.winner is self.winner_X:
            print "Case #%s: X won" % self.case_num
        elif self.winner is self.winner_O:
            print "Case #%s: O won" % self.case_num
        elif self.winner is self.winner_DRAW:
            print "Case #%s: Draw" % self.case_num
        elif self.winner is self.winner_INCOMPLETE:
            print "Case #%s: Game has not completed" % self.case_num
        else:
            print "Error"




# run it
try:
    f = open(sys.argv[1], 'r')
except:
    print 'Error opening file'
    sys.exit(0)

total_cases = None
board = ''
boards = []
while 1:
    line = f.readline()
    if not line:
        break

    try:
        if not total_cases and int(line):
            total_cases = int(line)
            line = f.readline()
    except:
        pass

    if len(line) <= 1:
        board = ''

    if len(line) > 1:
        board += line

    if len(board.splitlines()) == 4:
        boards.append(board)

##print "test cases:", total_cases
##print "boards:", boards

for i in range(0, total_cases):
    b = Board(i+1, boards[i])
    b.print_result()
