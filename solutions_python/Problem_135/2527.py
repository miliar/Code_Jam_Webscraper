import sys

__author__ = 'laurens'


class Game:
    def __init__(self, first_b, second_b, first_r, second_r):
        self.bad_magician = 'Bad magician!'
        self.volunteer_cheated = 'Volunteer cheated!'

        self.first_board = first_b
        self.second_board = second_b
        self.first_row = first_r
        self.second_row = second_r

    def get_solution(self):
        first_c = self.first_board[self.first_row -1]
        second_c = self.second_board[self.second_row - 1]
        candidates = set(first_c) & set(second_c)

        if len(candidates) == 0:
            return self.volunteer_cheated
        elif len(candidates) > 1:
            return self.bad_magician
        else:
            return candidates.pop()



file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')

tests = int(file_in.readline())

for x in range(0, tests):
    first_row = int(file_in.readline())
    first_board = [[int(x) for x in file_in.readline().split()] for x in range(0, 4)]
    second_row = int(file_in.readline())
    second_board = [[int(x) for x in file_in.readline().split()] for x in range(0, 4)]

    game = Game(first_board, second_board, first_row, second_row)

    file_out.write(('Case #' + str(x + 1) + ': ' + str(game.get_solution()) + '\n'))