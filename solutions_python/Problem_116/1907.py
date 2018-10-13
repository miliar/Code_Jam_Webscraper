#https://code.google.com/codejam/contest/2270488/dashboard

class TicTacToeTomek:
    # @param board: 2 dimensional 4x4 array specifying the tic tac toe tomek board
    def __init__(self, board):
        self.board = board

    def four_in_a_row(self, row):
        """ does @param row win the game? """
        values = set(row)
        needed_length = 1

        if '.' in values:
            self.spotted_dot = True
            return False

        if 'T' in values:
            needed_length += 1

        if len(values) == needed_length:
            if 'X' in values:
                self.winning_message = "X won"
            else:
                self.winning_message = "O won"
            return True

        return False

    def winner_message(self):
        """ get message about who the winner is """
        self.spotted_dot = False

        # search rows
        for i in range(4):
            if self.four_in_a_row(self.board[i]):
                return self.winning_message

        # search columns
        for j in range(4):
            if self.four_in_a_row([self.board[i][j] for i in range(4)]):
                return self.winning_message

        # search diagonals
        if self.four_in_a_row([self.board[i][i] for i in range(4)]) or \
           self.four_in_a_row([self.board[i][3-i] for i in range(4)]):
               return self.winning_message

        if(self.spotted_dot):
            return "Game has not completed"

        return "Draw"

if __name__ == "__main__":
    test_cases = input()
    for i in range(test_cases):
        board = []
        for _ in range(4):
            board.append(list(raw_input()))
        tttt = TicTacToeTomek(board)
        print "Case #" + str(i+1) + ": " + tttt.winner_message()
        raw_input()
