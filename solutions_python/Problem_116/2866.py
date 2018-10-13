from wxPython._wx import true

__author__ = 'andrey'

import sys


class Game:
    def __init__(self):
        self.board = {}.fromkeys(
            [(x, y) for x in xrange(4) for y in xrange(4)], 0)
        self._winner = 'X'

    def set_field(self, coordinate, value):
        self.board[coordinate] = value

    def c(self, first_coordinate, second_coordinate):
        """
        compare function return True or False
        """
        if (self.board[first_coordinate] == 'T' or
            self.board[second_coordinate] == 'T'):
            return True
        if (self.board[first_coordinate] == '.' or
            self.board[second_coordinate] == '.'):
            return False
        if self.board[first_coordinate] == self.board[second_coordinate]:
            return True
        else:
            return False

    def select_non_t(self, coordinate_1, coordinate_2,
                     coordinate_3, coordinate_4):
        if self.board[coordinate_1] != 'T':
            return self.board[coordinate_1]
        elif self.board[coordinate_2] != 'T':
            return self.board[coordinate_2]
        elif self.board[coordinate_3] != 'T':
            return self.board[coordinate_3]
        else:
            return self.board[coordinate_4]

    def check_no_free_space(self):
        return not '.' in self.board.values()

    def check_diagonal(self):
        if (self.c((0, 0), (1, 1)) and self.c((1, 1), (2, 2)) and
            self.c((2, 2), (3, 3))) and self.c((0, 0), (3, 3)):
            self._winner = self.select_non_t((0, 0), (1, 1), (2, 2), (3, 3))
            return True
        elif (self.c((0, 3), (1, 2)) and self.c((1, 2), (2, 1)) and
            self.c((2, 1), (3, 0)) and self.c((0, 3), (3, 0))):
            self._winner = self.select_non_t((0, 3), (1, 2), (2, 1), (3, 0))
            return True
        else:
            return False

    def check_horizontal(self):
        for i in xrange(4):
            if (self.c((i, 0), (i, 1)) and self.c((i, 1), (i, 2)) and
                    self.c((i, 2), (i, 3))):
                self._winner = self.select_non_t((i, 0), (i, 1), (i, 2), (i, 3))
                return True
        return False

    def check_vertical(self):
        for i in xrange(4):
            if (self.c((0, i), (1, i)) and self.c((1, i), (2, i)) and
                    self.c((2, i), (3, i))):
                self._winner = self.select_non_t((0, i), (1, i), (2, i), (3, i))
                return True
        return False

    def get_winner(self):
        if (self.check_diagonal() or
            self.check_horizontal() or
            self.check_vertical()):
            return self._winner + u" won"
        if self.check_no_free_space():
            return u"Draw"
        else:
            return u"Game has not completed"


class FileIterator:
    def __init__(self, name = None):
        self.file = open(name, 'r', False)
        self.num = int(self.file.readline())
        self.current_num = 0
        self.game = None

    def __iter__(self):
        return self

    def next(self):
        self.game = None
        self.current_num += 1
        if self.current_num > self.num:
            raise StopIteration
        self.game = self.read_one_game_data()
        return self.game.get_winner()

    def read_one_game_data(self):
        game = Game()
        for i in xrange(4):
            one_str = self.file.readline()
            for j in xrange(len(one_str)):
                game.set_field((i, j), one_str[j])
        self.file.readline()
        return game

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == "__main__":

    case_number = 0
    format_string = u"Case #%d: %s\n"
    out = file(sys.argv[2], 'wt')

    for f in FileIterator(sys.argv[1]):
        case_number += 1
        result_string = format_string % (case_number, f)
        print result_string
        out.write(result_string)

    out.close()


