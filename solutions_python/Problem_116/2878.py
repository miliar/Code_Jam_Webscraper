class GameStatus(object):
    X_WON = 0
    O_WON = 1
    DRAW = 2
    IN_PROGRESS = 3
    UNKNOWN = 4

    STATUS_MESSAGES = {
        X_WON: "X won",
        O_WON: "O won",
        DRAW: "Draw",
        IN_PROGRESS: "Game has not completed",
        }
    
class Symbols(object):
    X_SYMB = 'X'
    O_SYMB = 'O'
    JOKER = 'T'
    EMPTY = '.'

class GameBoard(object):
    '''
    @input: board_content - a list of strings, each representing a row in the board.
    '''
    def __init__(self, board_content):
        self._rows = board_content
        self._cols = [''.join(x) for x in list(zip(*board_content))]
        self._status = GameStatus.UNKNOWN
        
    def determine_status(self,):
        self._status = GameStatus.DRAW
        # generating the diagonal
        diag1 = [''.join(self._rows[i][i] for i in range(len(self._rows)))]
        diag_2_indexes = list(zip(range(len(self._rows)-1, -1, -1), range(len(self._cols))))
        diag2 = [''.join(self._rows[i][j] for i,j in diag_2_indexes)]
        for element in self._rows + self._cols + diag1 + diag2:
            #import pdb
            #pdb.set_trace()
            first = element[0] if element[0] != Symbols.JOKER else element[1]
            found = True
            for symbol in element:
                if symbol == Symbols.EMPTY:
                    self._status = GameStatus.IN_PROGRESS
                    found = False
                    break
                elif symbol != first and symbol != Symbols.JOKER:
                    found = False
                    break
            if found:
                if first == Symbols.X_SYMB:
                    self._status = GameStatus.X_WON
                if first == Symbols.O_SYMB:
                    self._status = GameStatus.O_WON
                return
    
    def get_game_status_message(self,):
        if self._status == GameStatus.UNKNOWN:
            self.determine_status()
        return GameStatus.STATUS_MESSAGES[self._status]