
PROBLEM_ID = "C" # A B or C
PROBLEM_SIZE = "large"

# `impossible` look up tables, used as short cut
# G4[9] == IS_MINE means 9 mines for a 4 by 4 grid is impossible
# actually in my algorithm, it might just check G3[2] depending where I put this short-cut
# which gives the same answer, of course :)
# Note: index is 1-based for readability
I = []
I.append([])
I.append([None, 1])
I.append([None, 1, 1, 1, 1])
I.append([None, 0, 1, 0, 1, 0, 1, 1, 1, 1])
I.append([None, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1])
I.append([None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1])
IS_MINE = "*"
NOT_MINE = "."

def run():
    """
        I/O handler
    """
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    #print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def solve_case(in_f, out_f, case_index):
    """
        problem solver
    """
#    #print "Case #{}:".format(case_index)
    R, C, M = [int(x) for x in in_f.readline().rstrip('\n').split()]
#    #print R, C, M
    global G
    G = [[{"is_mine":NOT_MINE, "printable_v":"."} for x in range(C)] for y in range(R)]
    find_solution = solve(R, C, M)
    out_f.write("Case #{}:\n".format(case_index))
#    out_f.write("{} {} {}\n".format(R, C, M))

    if find_solution:
        print_solution(out_f)
    else:
        #print "case#{} {} {} {}".format(case_index, R, C, M)
        out_f.write("Impossible\n")
   
def solve(R, C, M):
    """
    None indicates not solvable at this point
    fill tiles from button -> up, right -> left
    So when we shrink the problem size, the G could be reused with natural indexes.
    """
    if not M:
        return True
    # handle special cases here
    if R * C - M == 1:
        mark_all_mines()
        return True
#    if 1 in (R, C):
#        mark_all_line()
#        return False
    if 2 in (R, C) and M % 2 == 1:
        return False
    # not a square, trying to reduce it towards a square!
    if R > C:
        if M >= C:
            mark_button_row(R, C, C)
            return solve(R-1, C, M-C)
        mark_bottom_two_rows(R, C, M)
        return True
    elif C > R:
        if M >= R:
            mark_right_column(C)
            return solve(R, C-1, M-R)
        mark_right_two_columns(R, C, M)
        return True
    # we have perfect solution for square!
    if M >= 2*R-1:
        mark_button_and_right_mines(R)
        return solve(R-1, C-1, M+1-2*R)

    if R <= 5 and I[R][M]: 
        # short cut for these. we got solution for these!
        # also this gives me confident to safely put two lines if we need in the later section.
        #print "Impossible by checking I[{}][{}]".format(R, M)
        return False

    # always have a solution here!
    if M == R-1: 
        mark_bottom_two_rows(R, C, M)
        #print "mark them in two bottom lines, one for C-2, second for M+2-C I[{}][{}]".format(R, M)
        return True
    else: # safe to mark them from right bottom to top left.
        #print "safe to mark them from right bottom to top left. I[{}][{}]".format(R, M)
        if M <= C:
            mark_button_row(R, C, M)
        else:
            mark_button_row(R, C, C)
            mark_button_row(R-1, C, M-C)
        return True

def mark_right_two_columns(R, C, M):
    """
    mark them in two right columns, one for R-2, second for M+2-R
    """
    global G
    if M <= R-2:
        for x in range(0, M): # right most column
            G[R-x-1][C-1]["is_mine"] = IS_MINE
    else:
        for x in range(0, R-2): # right most column
            G[R-x-1][C-1]["is_mine"] = IS_MINE
        for x in range(0, M+2-R): # next buttom row
            #print "222"
            G[R-x-1][C-2]["is_mine"] = IS_MINE
    inspect()
            
def mark_bottom_two_rows(R, C, M):
    """
    mark them in two bottom lines, one for C-2, second for M+2-C
    """
    global G
    if M <= C-2:
        for x in range(0, M): # buttom row
            G[R-1][C-x-1]["is_mine"] = IS_MINE
    else:
        for x in range(0, C-2): # buttom row
            G[R-1][C-x-1]["is_mine"] = IS_MINE
        for x in range(0, M+2-C): # next buttom row
            G[R-2][C-x-1]["is_mine"] = IS_MINE
    inspect()
            
def mark_button_row(R, C, M):
    """
    Reduce the problem size by marking mines on the button row
    R is the grid row for current iteration
    """
    global G
    for x in range(0, M): # buttom row
        G[R-1][C-x-1]["is_mine"] = IS_MINE
    inspect()

def mark_right_column(C):
    """
    Reduce the problem size by marking mines on right column
    C is the grid column for current iteration
    """
    global G
    for tile in [row[C-1] for row in G]:
        tile["is_mine"] = IS_MINE
    inspect()

def mark_button_and_right_mines(R):
    """
    Reduce the problem size by marking mines on the button row & right column
    R is the grid size for current iteration
    """
    global G
    for tile in G[R-1]: # button row
        tile["is_mine"] = IS_MINE
    for tile in [row[R-1] for row in G]: # right column
        tile["is_mine"] = IS_MINE
    inspect()

def inspect(type="is_mine", message=None):
    """test function"""
    return
    global G
    for row in G:
        print[tile[type] for tile in row]

def mark_all_mines():
    """used to support 3 4 11 -- only one which is not mine could mark as c!"""
    global G
    for row in G:
        for tile in row:
            tile["is_mine"] = IS_MINE


def print_solution(out_f, type="is_mine", message=None):
    """chose top left tile as C"""
    global G
    G[0][0][type] = "c"
    
    for row in G:
        line = "".join([tile[type] for tile in row])
        #print line
        out_f.write("{}\n".format(line))
run()
