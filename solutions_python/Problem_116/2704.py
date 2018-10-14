def check_rows(str_list):# check rows
    count_d = 0
    for val in str_list:
        str = ''.join(val)
        count_x = str.count('X')            
        count_y = str.count('O')
        count_d += str.count('.')
        count_t = str.count('T')
        if(count_x >= 3 and count_y == 0 and count_t <= 1):
            return 'X won'
        if(count_y >= 3 and count_x == 0 and count_t <= 1):
            return 'O won'
    if count_d > 0:
        return "Game has not completed"
    return 'Draw'
        
def check_win(c_state):
    # check rows:
    win = check_rows(c_state)    
    # check cols
    if win == 'Game has not completed' or win == 'Draw':
        c_state_T = map(list, zip(*c_state))
        win = check_rows(c_state_T)
    return win

def main():
    T = raw_input('')
    allInput = {}
    
    for case in xrange(0, int(T)):#for each test case
        inputs = []
        for row in xrange(0, 4):
            inp = raw_input('')
            inputs.append(list(inp))
        blank_line = raw_input()
        allInput[case] = inputs
    for case in allInput:        
        incomplete = 0
        win = check_win(allInput[case])
        if win == 'Game has not completed' or win == 'Draw':
            if win == 'Game has not completed':
                incomplete = 1                
            d1_str = [allInput[case][i][i] for i in range(4)]
            d2_str = [allInput[case][i][3 - i] for i in range(4)]
            win = check_rows([d1_str, d2_str])
            if win == 'Draw' and incomplete == 1:
                win = 'Game has not completed'
        print "Case #" + str(case+1) + ": " + win
        
if __name__ == "__main__":
    main()