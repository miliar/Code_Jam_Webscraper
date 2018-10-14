import sys

# map the result string
result_tbl = [
    "O won",
    "X won",
    "Draw",
    "Game has not completed"
]

class game:
    '''
    Defines the game abstraction
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.__game = ['....'] * 4  # game board 4x4
        self.__current_line = 0     # current line parsed
        self.__result = -1          # game final status

    def add(self, line):
        '''
        Adds the line from the test case in
        the game board

        @type  line: basestring
        @param line: game line of 4 bytes

        @rtype:   nothing
        @returns: nothing
        '''
        self.__game[self.__current_line] = line
        self.__current_line += 1
    # add()

    def __check(self, line):
        '''
        Checks the if the line has a game completed

        <private>

        @type  line: basestring
        @param line: game line of 4 bytes

        @rtype:   int
        @returns: 0 if O win, 1 if X win, -1 if none
        '''
        t_idx   = line.find('T')      # find the joker T
        x_count = line.count('X')   # number of Xs found in line
        o_count = line.count('O')   # number of Os found in line

        # O completes a line (with or without T)
        if o_count == 4 or (o_count == 3 and t_idx > -1):
            return 0

        # X completes a line (with or without T)
        elif x_count == 4 or (x_count == 3 and t_idx > -1):
            return 1

        # nobody completes the line
        else:
            return -1
    # __check()

    def __check_lines(self):
        '''
        Checks each line of the game board for a winner

        <private>

        @rtype:   int
        @returns: 0 if O win, 1 if X win, -1 if none
        '''
        for line in self.__game:
            ret = self.__check(line)
            if ret != -1:
                return ret

        return -1
    # __check_lines()

    def __check_columns(self):
        '''
        Checks each column of the game board for a winner

        <private>

        @rtype:   int
        @returns: 0 if O win, 1 if X win, -1 if none
        '''
        # create a string of each column and check for a
        # winner using __check()
        for i in xrange(0, 4):

            column = ''
            for j in xrange(0, 4):

                # transform the column in a string
                column += self.__game[j][i]

            res = self.__check(column)
            if res != -1:
                return res

        return -1
    # __check_columns()

    def __check_diagonals(self):
        '''
        Checks diagonals of the game board for a winner
        00, 11, 22, 33
        03, 12, 21, 30

        <private>

        @rtype:   int
        @returns: 0 if O win, 1 if X win, -1 if none
        '''
        cell   = '' # main diagonal
        cell_i = '' # anti diagonal

        # create strings for both main and anti diagonals
        # and check for a winner using __check()
        for i in xrange(0, 4):
            cell   += self.__game[i][i]    # 00 11 22 33
            cell_i += self.__game[i][3-i]  # 03 12 21 30

        # main diagonal has winner, return it
        chk = self.__check(cell)
        if chk != -1:
            return chk
        
        # check anti diagonal and return
        return self.__check(cell_i)
    # __check_diagonals()

    def __has_empty_cell(self):
        '''
        Checks if there is any empty cell in the
        game board

        <private>

        @rtype:   bool
        @returns: True if it has empty space, False otherwise
        '''
        for item in self.__game:
            if item.find('.') > -1 :
                return True

        return False
    # __has_empty_cell()

    def validate_game(self):
        '''
        Computes the current game status and stores
        the result

        @rtype:   nothing
        @returns: nothing
        '''
        # check for a winner (rows)
        result = self.__check_lines()
        if result != -1:
            self.__result = result
            return

        # check for a winner (columns)
        result = self.__check_columns()
        if result != -1:
            self.__result = result
            return

        # check for a winner (diagonals)
        result = self.__check_diagonals()
        if result != -1:
            self.__result = result
            return

        # game not yet completed
        if not self.__has_empty_cell():
            self.__result = 2
            return
        
        # game draw
        self.__result = 3
    # validate_game()

    def print_results(self, test_num):
        '''
        Prints the result in stdout according
        to the requirements

        @type test_num:  int
        @param test_num: test case number

        @rtype:   nothing
        @returns: nothing
        '''
        print "Case #%d: %s" % (test_num + 1,
                                result_tbl[self.__result])
    # print_results()
# class game

def main(lines):
    
    # get the number of test cases
    num_test_cases = int(lines[0])
    
    games = []

    tmp_game = game()
    for line in lines[1:]:

        # remove \n
        line = line[:-1]

        # initialize a new game (test case)
        # when a empty space is found
        if len(line) != 4:
            games.append(tmp_game)
            tmp_game = game()
            continue

        # add item in game
        tmp_game.add(line)

    # validade parsed games x num test cases
    if num_test_cases != len(games):
        exit(1)

    i = 0
    for tictac in games:

        # check current games status
        tictac.validate_game()

        # print output to stdout
        tictac.print_results(i)
        i += 1
# main()

if __name__ == "__main__":
    main(sys.stdin.readlines())
