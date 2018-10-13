import StringIO
import random

from ecodejam import backtrack
from ecodejam.backtrack import GameState
from ecodejam.input_parser import *

# scores:
#
# . = 0
# + = 1
# x = 1
# o = 2

HAS_PLUS = 1
HAS_X = 2
HAS_O = 4

MODEL_TO_FLAG = {
    ".": 0,
    "+": HAS_PLUS,
    "x": HAS_X,
    "o": HAS_O,
}

MODEL_TO_SCORE = {
    ".": 0,
    "+": 1,
    "x": 1,
    "o": 2,
}


class IllegalMove(Exception):
    pass


max_score = None
max_board = None


def clear_max_board():
    global max_score, max_board
    max_score = None
    max_board = None


def global_callback(cur_board):
    global max_score, max_board

    cur_score = cur_board.get_score()
    if max_score is None or cur_score > max_score:
        max_score = cur_score
        max_board = cur_board
        print "****"
        print max_score
        max_board.printb()


class ModelsGameState(GameState):
    def __init__(self, n):
        self.n = n
        self.states = {
            "row": [0] * self.n,                 # -
            "col": [0] * self.n,                 # |
            "diag1": [0] * (2 * self.n - 1),     # \
            "diag2": [0] * (2 * self.n - 1),     # /
        }

        self.board = [
            ["." for _ in xrange(self.n)]
            for _ in xrange(self.n)
        ]

    def dup(self):
        ret = ModelsGameState(self.n)

        ret.states = {
            key: list(value)
            for key, value in self.states.iteritems()
        }

        ret.board = [
            list(row)
            for row in self.board
        ]

        return ret

    def is_solved(self):
        return False

    def solve_comb(self):
        global_callback(self)
        return self

    def guess_iter(self):
        for row in xrange(self.n):
            for col in xrange(self.n):
                cur = self.board[row][col]

                if cur != "o":
                    try:
                        yield self.dup().place(row, col, "o")
                    except IllegalMove:
                        pass

                if cur == ".":
                    try:
                        yield self.dup().place(row, col, "+")
                    except IllegalMove:
                        pass

                    try:
                        yield self.dup().place(row, col, "x")
                    except IllegalMove:
                        pass

    def printb(self):
        for line in self.board:
            print "".join(line)

    def get_score(self):
        return sum(
            MODEL_TO_SCORE[self.board[i][j]]
            for i in xrange(self.n)
            for j in xrange(self.n)
        )

    def state_index(self, row, col):
        return {
            "row": row,
            "col": col,
            "diag1": (self.n - 1) + (row - col),
            "diag2": row + col
        }

    def place(self, row, col, model):
        before_state = MODEL_TO_FLAG[self.board[row][col]]
        for state, index in self.state_index(row, col).iteritems():
            self.states[state][index] &= ~before_state
        self.board[row][col] = model
        after_state = MODEL_TO_FLAG[model]

        state_index = self.state_index(row, col)

        if model == "x" or model == "o":
            for state, index in state_index.iteritems():
                if state in {"row", "col"} and self.states[state][index] & (HAS_O | HAS_X):
                    raise IllegalMove
        if model == "+" or model == "o":
            for state, index in state_index.iteritems():
                if state in {"diag1", "diag2"} and self.states[state][index] & (HAS_O | HAS_PLUS):
                    raise IllegalMove

        for state, index in state_index.iteritems():
            self.states[state][index] |= after_state
        return self


def enrich_for_small(game):
    if any(game.board[0][i] == "x" for i in xrange(0, game.n)):
        x_index = [i for i in xrange(0, game.n) if game.board[0][i] == "x"][0]
        game.place(0, x_index, "o")

    if not any(game.board[0][i] == "o" for i in xrange(0, game.n)):
        game.place(0, random.randrange(0, game.n), "o")

    for i in xrange(0, game.n):
        if game.board[0][i] == ".":
            game.place(0, i, "+")

    o_index = [i for i in xrange(0, game.n) if game.board[0][i] == "o"][0]

    for row, col in enumerate(xrange(o_index-1, -1, -1), 1):
        game.place(row, col, "x")

    for i in xrange(o_index + 1, game.n):
        game.place(i, i, "x")

    for i in xrange(1, game.n - 1):
        game.place(game.n - 1, i, "+")


def ret_str(game1, game2):
    ret = ""

    changes = 0
    for row in xrange(game1.n):
        for col in xrange(game1.n):
            if game1.board[row][col] != game2.board[row][col]:
                changes += 1
                ret += "{} {} {}\n".format(game2.board[row][col], row + 1, col + 1)

    return ("{} {}\n".format(game2.get_score(), changes) + ret).strip()


def solve_backtrack(game):
    start = game.dup()

    clear_max_board()
    backtrack.backtrack(game, False)
    max_board.printb()

    return ret_str(start, max_board)
    # return ""


def solve_small(case_index):
    print case_index
    n = read_int()
    m = read_int()
    next_line()

    game = ModelsGameState(n)

    for i in xrange(m):
        model = read_word()
        row = read_int() - 1
        col = read_int() - 1
        game.place(row, col, model)
        next_line()

    if n <= 2:
        return solve_backtrack(game)

    start = game.dup()

    enrich_for_small(game)

    return ret_str(start, game)
    # return "{} {}".format(game.get_score(), 3 * game.n - 2)

solve = solve_small

# SAMPLE = """
# 3
# 2 0
# 1 1
# o 1 1
# 3 4
# + 2 3
# + 2 1
# x 3 1
# + 2 2
# """

# SAMPLE = """
# 1
# 8 8
# o 1 4
# o 2 6
# o 3 8
# o 4 2
# o 5 7
# o 6 1
# o 7 3
# o 8 5
# """

SAMPLE = """
"""


if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
