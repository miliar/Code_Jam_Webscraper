#!/usr/bin/python

###
# Definitions and files to open
###
out_array = []
source_file = 'Q1.txt'

try:
    f = open(source_file)
except IOError:
    print ('could not open source file ' + source_file)

###
# Classes we need
###

class game:
    # This class takes all of the inputs to one of the games: the first row, 
    # the first 4x4 array, the second row called and the second 4x4 array.
    def __init__(self, call_1, array_1, call_2, array_2):
        self.row_1 = call_1 - 1
        self.array_1 = array_1
        self.row_2 = call_2 - 1
        self.array_2 = array_2

    # The evaluate method returns the string that should be used as "y" in 
    # the output for the game
    def evaluate(self):
        first_row = self.array_1[self.row_1]
        second_row = self.array_2[self.row_2]
        success = 0
        
        ###
        # For every pair of numbers that match between the two rows, record
        # the pair and add one to the success value, as this represents a
        # possible value of the volunteer's card. If the game was done
        # right, there should be a unique such pair.
        ###
        for num_1 in first_row:
            for num_2 in second_row:
                print('Comparing {0} to {1}'.format(str(num_1), str(num_2)))
                if num_2 == num_1:
                    print('yup')
                    success = success + 1
                    out_num = num_2

        if success == 0:
            out_str = "Volunteer cheated!"
        elif success == 1:
            out_str = str(out_num)
        else:
            out_str = 'Bad magician!'

        return out_str

    # The play method plays a game and outputs a string of the result.
    # The num param refers to what number the game is in sequnce.
    def play(self, num):
        result = self.evaluate()
        out_str = 'Case #' + str(num + 1) + ': ' + result
        return out_str

###
# Parse the input and play the games
###

num_games = int(f.readline().rstrip())

for ii in range(num_games):
    game_array_1 = []
    game_array_2 = []
    call_1 = int(f.readline().rstrip())
    for jj in range(4):
        game_array_1.append(f.readline().rstrip().split())
    call_2 = int(f.readline().rstrip())
    for jj in range(4):
        game_array_2.append(f.readline().rstrip().split())

    current_game = game(call_1, game_array_1, call_2, game_array_2)
    out_array.append(current_game.play(ii))

###
# Print the results
###

for out_line in out_array:
    print(out_line)


