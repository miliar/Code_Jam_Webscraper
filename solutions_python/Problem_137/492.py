#!/usr/bin/python

###
# Definitions and files to open
###
out_array = []
source_file = 'Q3.txt'

try:
    f = open(source_file)
except IOError:
    print ('could not open source file ' + source_file)

###
# Classes we need
###

class Game:
    def __init__(self, rr, cc, mm):
        self.width = cc;
        self.height = rr;
        self.mines = mm;
        cells = self.width * self.height
        self.empty_cells = cells - self.mines
        if rr == 1:
            if cc == 1:
                self.type = '1'
            else:
                self.type = 'r_1'
        else:
            if cc == 1:
                self.type = 'c_1'
            else:
                self.type = "2"
        return

    def doable(self):
        doable = False
        # Neither of r and c can be 0.
        # If r is 1 or c is 1 we only need one empty cell
        # Else we need 4 at one corner.
        # Turns out this heuristic is bad, but at least it catches
        # some obviously impossible cases
        if self.type == '1':
            if self.empty_cells >= 1:
                doable = True
        elif (self.type == 'r_1') or (self.type == 'c_1'):
            if self.empty_cells >= 1:
                doable = True
        else:
            if self.empty_cells >= 4:
                doable = True
            elif self.empty_cells == 1:
                doable = True
        return doable

    def solve(self):
        # This method prints(!) the desired output for this round
        if self.doable() == False:
            print("Impossible")
        else:
            # This is doable.
            # Delegate to the relevant method.
            if self.type == '1':
                self.solve_1()
            elif self.type == 'r_1':
                self.solve_r_1()
            elif self.type == 'c_1':
                self.solve_c_1()
            else:
                self.solve_2()
        return

    def solve_2(self):
        # Extra escape bit for the stupid case I forgot about!
        if self.empty_cells == 1:
            # Only one empty cell! This is obvious right?
            row_1_print = 'c'
            for ii in range(self.width - 1):
                row_1_print += '*'
            print(row_1_print)
            for ii in range(self.height - 1):
                row_print = ''
                for jj in range(self.width):
                    row_print += '*'
                print(row_print)
            return

        # This method prints the desired output for a game with 2 or more cols
        # and 2 or more rows. The way to do it is to fill up the top two rows 
        # from the left, then each row downwards from the left.
        two_rows = (self.empty_cells >= (2 * self.width))
        if not two_rows:
            # Don't have enough for two rows.  Fill from the left as evenly as
            # possible, tie-breaking for the first row.
            row_2 = self.empty_cells // 2
            row_1 = self.empty_cells - row_2
            if (row_1 == row_2):
                # print row 1, with clicking at top left.
                row_1_print = 'c'
                for ii in range(row_1 - 1):
                    row_1_print += '.'
                for ii in range(self.width - row_1):
                    row_1_print += '*'
                print(row_1_print)
                # print row 2.
                row_2_print = ''
                for ii in range(row_2):
                    row_2_print += '.'
                for ii in range(self.width - row_2):
                    row_2_print += '*'
                print(row_2_print)
                # print any further rows.
                for ii in range(self.height - 2):
                    row_print = ''
                    for jj in range(self.width):
                        row_print += '*'
                    print(row_print)
                # and we're done!
                return
            else:
                # Our first two rows are unbalanced.
                # If we have more than 9, and more than 3 rows, stick 3 on the
                # next row.
                if (self.empty_cells >= 9) and (self.height >= 3):
                    row_1 -= 2
                    row_2 -= 1
                    row_3 = 3
                    #print row 1
                    row_1_print = 'c'
                    for ii in range(row_1 - 1):
                        row_1_print += '.'
                    for ii in range(self.width - row_1):
                        row_1_print += '*'
                    print(row_1_print)
                    # print row 2.
                    row_2_print = ''
                    for ii in range(row_2):
                        row_2_print += '.'
                    for ii in range(self.width - row_2):
                        row_2_print += '*'
                    print(row_2_print)
                    # print row 3.
                    row_3_print = ''
                    for ii in range(row_3):
                        row_3_print += '.'
                    for ii in range(self.width - row_3):
                        row_3_print += '*'
                    print(row_3_print)                
                    # print any further rows.
                    for ii in range(self.height - 3):
                        row_print = ''
                        for jj in range(self.width):
                            row_print += '*'
                        print(row_print)
                    # and we're done!   
                    return                     
                else:
                    print('Impossible')
                    return
        else:
            # Have enough for two rows. Work out which row will be incomplete, 
            # and how many are needed on that row.
            full_rows = self.empty_cells // self.width
            remainder = self.empty_cells % self.width
            mine_rows = self.mines // self.width
            if not remainder == 1:
                # Fill in row 1
                row_1_print = 'c'
                for ii in range(self.width - 1):
                    row_1_print += '.'
                print(row_1_print)
                # Fill in all the empty rows
                row_print = ''
                for jj in range(self.width):
                    row_print += '.'                
                for ii in range(full_rows - 1):
                    print(row_print)
                # Fill in the incomplete row, if there is one
                if not remainder == 0:
                    part_row_print = ''
                    for ii in range(remainder):
                        part_row_print += '.'
                    for ii in range(self.width - remainder):
                        part_row_print += '*'
                    print(part_row_print)
                # Fill in the full rows.
                row_print = ''
                for jj in range(self.width):
                    row_print += '*'                
                for ii in range(mine_rows):
                    print(row_print)  
                # That's all!
                return         
            else:
                # Remainder was 1. Having 1 sticking out the end is very very 
                # bad, so go into panic mode!
                # Possibilities:
                # If the number of columns is 2, we are surprised-screwed as in
                # the two full rows, odd empty squares, no third row case
                if self.width == 2:
                    print('Impossible')
                    return
                # If we have 3 or more full rows, we can redistribute the 
                # mines in the partial row and stick the first one on the end
                # of the previous row
                if full_rows >= 3:
                    # Fill in row 1
                    row_1_print = 'c'
                    for ii in range(self.width - 1):
                        row_1_print += '.'
                    print(row_1_print)
                    # Fill in all the empty rows bar 1
                    row_print = ''
                    for jj in range(self.width):
                        row_print += '.'                    
                    for ii in range(full_rows - 2):
                        print(row_print)
                    # Fill in the pre-incomplete row
                    pre_row_print = ''
                    for ii in range(self.width - 1):
                        pre_row_print += '.'
                    pre_row_print += '*'
                    print(pre_row_print)
                    # Fill in the incomplete row
                    part_row_print = ''
                    for ii in range(remainder + 1):
                        part_row_print += '.'
                    for ii in range(self.width - remainder - 1):
                        part_row_print += '*'
                    print(part_row_print)
                    # Fill in the full rows.
                    row_print = ''
                    for jj in range(self.width):
                        row_print += '*'                    
                    for ii in range(mine_rows):
                        print(row_print)  
                    # That's all!
                    return
                # If not, if the number of full rows is not a multiple of 
                # c - 1, then we can put mines all the way up the right hand edge 
                # to fix it.
                if not ((full_rows % (self.width - 1)) == 0):
                    # This solution basically looks like a width - 1 solution 
                    # with height fewer mines, and extra mines up the side.
                    n_width = self.width - 1
                    n_mines = self.mines - self.height
                    # There's no need for n_empty_cells because no empty cells
                    # go outside the new board size!
                    n_full_rows = self.empty_cells // n_width
                    n_remainder = self.empty_cells % n_width
                    n_mine_rows = n_mines // n_width
                    # Fill in row 1
                    row_1_print = 'c'
                    for ii in range(n_width - 1):
                        row_1_print += '.'
                    row_1_print += '*'
                    print(row_1_print)
                    # Fill in all the empty rows
                    row_print = ''
                    for jj in range(n_width):
                        row_print += '.'
                    row_print += '*'
                    for ii in range(n_full_rows - 1):
                        print(row_print)
                    # Fill in the incomplete row, if there is one
                    if not n_remainder == 0:
                        part_row_print = ''
                        for ii in range(n_remainder):
                            part_row_print += '.'
                        for ii in range(n_width - n_remainder + 1):
                            part_row_print += '*'
                        print(part_row_print)
                    # Fill in the full rows.
                    row_print = ''
                    for jj in range(self.width):
                        row_print += '*'
                    for ii in range(n_mine_rows):
                        print(row_print)  
                    # That's all!
                    return         
                # We wouldn't be here with only 1 full row, so the only error case
                # left is 2 full rows, 3 columns. So it looks exactly like this:
                # c.. And I think we look pretty screwed at this point!
                # ...
                # .**
                # ???
                print('Impossible')
                return

    def solve_c_1(self):
        # This method prints the desired output for a single column game.
        # Click the top square, have empty squares below that, then mines.
        print ('c')
        for ii in range(self.empty_cells - 1):
            print ('.')
        for ii in range(self.mines):
            print ('*')
        return

    def solve_r_1(self):
        # This method prints the desired output for a single row game.
        # Click the leftmost square, have empty squares on the right, then 
        # mines.
        printstr = 'c'
        for ii in range(self.empty_cells - 1):
            printstr += '.'
        for ii in range(self.mines):
            printstr += '*'
        print(printstr)
        return

    def solve_1(self):
        # This method prints the desired output for a 1x1 game.
        print('c')
        return

###
# Parse the input and print the results
###
num_games = int(f.readline().rstrip())

for ii in range(num_games):
    new_game = 0
    line = f.readline().rstrip().split()
    [rr, cc, mm] =  [int(jj) for jj in line]
    new_game = Game(rr, cc, mm)
    print('Case #' + str(ii + 1) + ':')
    new_game.solve()
