import os
import sys

abpath = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))


class TicTac(object):

    X_WON = 'X won'
    O_WON = 'O won'
    DRAW = 'Draw'
    NOT_COMPLETE = 'Game has not completed'
    GAME_BOARD = [[[], [], [], []],
                  [[], [], [], []],
                  [[], [], [], []],
                  [[], [], [], []]]

    num_cases = None
    current_board = None
    x_consec = 0
    o_consec = 0

    def __init__(self, in_fh, out_fh):
        self.num_cases = int(in_fh.readline())
        self.in_fh = in_fh
        self.out_fh = out_fh

    def solve_all(self):
        for i in range(self.num_cases):
            self.reset_board()
            self.build_board()
            state = self.solve_case()
            line_output = ''.join(('Case #', str(i + 1), ': ', state, '\n'))
            self.out_fh.write(line_output)

    def solve_case(self):
        outcome = self.solve_rows()
        if outcome == self.X_WON or outcome == self.O_WON:
            return outcome
        col_outcome = self.solve_cols()
        if col_outcome == self.X_WON or col_outcome == self.O_WON:
            return col_outcome
        diag_outcome = self.solve_diags()
        if diag_outcome == self.X_WON or diag_outcome == self.O_WON:
            return diag_outcome

        if outcome == self.DRAW:
            return self.DRAW
        else:
            return self.NOT_COMPLETE

    def solve_diags(self):
        total = self.current_board[0][0]
        total += self.current_board[1][1]
        total += self.current_board[2][2]
        total += self.current_board[3][3]
        if total == 9 or total == 12:
            return self.X_WON
        elif total == 21 or total == 28:
            return self.O_WON
        total = self.current_board[0][3]
        total += self.current_board[1][2]
        total += self.current_board[2][1]
        total += self.current_board[3][0]
        if total == 9 or total == 12:
            return self.X_WON
        elif total == 21 or total == 28:
            return self.O_WON

    def solve_cols(self):
        finished = False
        outcome = self.NOT_COMPLETE
        for col in range(4):
            total = 0
            for row in range(4):
                total += self.current_board[row][col]
            if total == 9 or total == 12:
                outcome = self.X_WON
                finished = True
            elif total == 21 or total == 28:
                outcome = self.O_WON
                finished = True
        return outcome

    def solve_rows(self):
        finished = False
        outcome = self.NOT_COMPLETE
        draw = True
        while not finished:
            for row in self.current_board:
                total = sum(row)
                if total == 9 or total == 12:
                    outcome = self.X_WON
                    finished = True
                elif total == 21 or total == 28:
                    outcome = self.O_WON
                    finished = True
                elif total >= 30:
                    draw = False
            finished = True
        if draw is True:
            outcome = self.DRAW
        return outcome

    def build_board(self):
        for i in range(4):
            line = self.next_line()
            self.set_board_line(i, line)

    def reset_board(self):
        self.current_board = self.GAME_BOARD

    def set_board_line(self, line_num, line):
        for x in range(0, len(line)):
            self.current_board[line_num][x] = self.set_board_square(line[x])

    def set_board_square(self, character):
        grid_val = 999
        if character == 'O':
            grid_val = 7
        elif character == 'X':
            grid_val = 3
        elif character == 'T':
            grid_val = 0
        elif character == '.':
            grid_val = 300
        return grid_val

    def next_line(self):
        get_line = lambda: self.in_fh.readline().strip()
        line = get_line()
        if not line:
            line = get_line()
        return line

    def write_line(self, fh):
        pass
        # write a line


def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    in_path = abpath('input/' + in_file)
    out_path = abpath('output/' + out_file)
    with open(in_path, 'r') as in_fh, open(out_path, 'w+') as out_fh:
        tictac = TicTac(in_fh, out_fh)
        tictac.solve_all()

if __name__ == '__main__':
    main()
