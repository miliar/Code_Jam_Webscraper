

win_patterns = ["XXXX", "OOOO", "XXX", "OOO"]

def tttt():
    """
        name is short for "Tic-Tac-Toe-Tomek"
    """
    in_f = open('A-large.in', 'r')
    out_f = open('output.txt', 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)
        
def solve_case(in_f, out_f, case_index):
    """
    get file object to continue reading the case
    """
    print "start handling case #{}".format(case_index)
    is_solved = False
    # used to dertermine if this is a draw
    is_finished = True
    board = [[0 for x in xrange(4)] for x in xrange(4)] 
    # each case contins 5 lines with last line being empty line
    # do the board initialiaztion and at the same time, 
    # if there is a quick win by line, quit quickly by just finishing reading all the remaining lines. 
    for j in range(1, 6):
        line = in_f.readline().rstrip('\n')
        if not is_solved and j != 5:
            print list(line)
            if is_finished and "." in line:
                is_finished = False
            # quick win by line
            is_win, winner = test_winning(line, out_f, case_index)
            if is_win:
                print "Quick Win by Line: {}".format(line)
                is_solved = True
            else:
                #store in board
                board[j-1] = list(line)
    print board
    if is_solved:
        return
    # start row testing
    for i in range(0,4):
        column = [row[i] for row in board]
        column_str = ''.join(column)
        is_win, winner = test_winning(column_str, out_f, case_index)
        if is_win:
            print "Win by Column: {}".format(column)
            return
    # start diagonal testing
    diagonal_1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
    diagonal_1_str = ''.join(diagonal_1)
    is_win, winner = test_winning(diagonal_1_str, out_f, case_index)
    if is_win:
        print "Win by diagonal: {}".format(diagonal_1)
        return
    diagonal_2 = [board[0][3], board[1][2], board[2][1], board[3][0]]
    diagonal_2_str = ''.join(diagonal_2)
    is_win, winner = test_winning(diagonal_2_str, out_f, case_index)
    if is_win:
        print "Win by diagonal: {}".format(diagonal_2)
        return
    # start testing if this is a draw
    if is_finished:
        out_f.write("Case #{}: Draw\n".format(case_index))
    else:
        out_f.write("Case #{}: Game has not completed\n".format(case_index))
        
def test_winning(str, out_f, case_index):
    """
    returns (true, winner) if the str passed indicates a win
    else return (false, None)
    """
    removed_t = str.replace("T","")
    if removed_t in win_patterns:
        winner = removed_t[0]
        out_f.write("Case #{}: {} won\n".format(case_index, winner))    
        return (True, winner)
    return (False, None)
    
if __name__ == '__main__':
    tttt()
