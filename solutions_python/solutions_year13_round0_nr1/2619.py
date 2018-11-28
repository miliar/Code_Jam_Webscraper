
import unittest


class Board(object):
    def __init__(self, cells, width=4, height=4):
        self.ANY_PLAYER = 'T'
        self.EMPTY = '.'
        self._cells = cells
        self.width = 4
        self.height = 4
    
    def cell(self, x, y):
        return self._cells[(y * self.width) + x]

    def _player_positions(self, player):
        return {(x, y) for x in range(self.width) 
                       for y in range(self.height)
                       if self.cell(x, y) == player}

    def is_winner(self, player):
        directions = [(x, y) for x in range(-1, 2)
                             for y in range(-1, 2)]
        directions.remove((0, 0))
        return any(self._brute_force_is_winner(player, position, direction)
                   for position in self._player_positions(player)
                   for direction in directions)

    def in_progress(self):
        return self.EMPTY in self._cells

    def _in_bounds(self, x, y):
        return ((x >= 0 and x < self.width)
                and (y >= 0 and y < self.height))
                
    def _brute_force_is_winner(self, player, position, direction, hit_count=0):
        x, y = position
        if self.cell(x, y) not in (player, self.ANY_PLAYER,):
            return False
        
        hit_count += 1
        if hit_count == 4:
            return True
        
        (x_direction, y_direction) = direction
        next_x = x + x_direction
        next_y = y + y_direction
        if self._in_bounds(next_x, next_y):
             return self._brute_force_is_winner(player, (next_x, next_y), direction, hit_count)
        return False

    def result(self):
        if self.is_winner('X'):
            return "X won"
        elif self.is_winner('O'):
            return "O won"
        elif self.in_progress():
            return "Game has not completed"
        else:
            return "Draw"


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.in_progress_board = Board("...."
                                       ".XO."
                                       "...."
                                       "....")
        self.x_winner = Board("XXXT....OO......")
        self.o_winner = Board("XXXO..O..O..T...")
    
    def test_cell_at(self):
        self.assertEqual('X', self.in_progress_board.cell(1, 1))
        self.assertEqual('O', self.in_progress_board.cell(2, 1))

    def test_player_positions(self):
        self.assertEqual(set(((1, 1),)),
                         self.in_progress_board._player_positions('X'))
    
    def test_is_winner(self):
        self.assertFalse(self.in_progress_board.is_winner('X'))
        self.assertTrue(self.x_winner.is_winner('X'))
        self.assertFalse(self.x_winner.is_winner('O'))
        self.assertTrue(self.o_winner.is_winner('O'))
        self.assertFalse(self.o_winner.is_winner('X'))
    

if __name__ == '__main__':
    board_count = int(raw_input())
    boards = []
    for n in range(board_count):
        boards.append(Board(''.join(raw_input() for i in range(4))))
        assert raw_input() == ''
    
    for n in range(board_count):
        print "Case #{}: {}".format(n+1, boards[n].result())





