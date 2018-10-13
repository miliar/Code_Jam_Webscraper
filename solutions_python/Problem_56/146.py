import sys

LINES_PER_CASE = 1

def printm(matrix):
    for row in matrix:
        print row

def line_to_ints(line):
    return [int(num) for num in line.split()]

def do_gravity(matrix):
    n = len(matrix)
    return [row.replace(".", "").rjust(n, ".") for row in matrix]

def get_winner_at(i, j, matrix, must_connect):
    n = len(matrix)
    piece = matrix[i][j]
    
    if piece != ".":
        win = [piece] * must_connect
        can_horiz = j + must_connect <= n
        can_vert = i + must_connect <= n
        can_diag_fwd = can_vert and can_horiz
        can_diag_bak = can_vert and (j - must_connect >= -1)
        
        horizontal = []
        vertical = []
        diag_fwd = []
        diag_bak = []
        
        for k in xrange(must_connect):
            if can_horiz:
                horizontal.append(matrix[i][j + k])
            
            if can_vert:
                vertical.append(matrix[i + k][j])
            
            if can_diag_fwd:
                diag_fwd.append(matrix[i + k][j + k])
            
            if can_diag_bak:
                diag_bak.append(matrix[i + k][j - k])
        
        if win in (horizontal, vertical, diag_fwd, diag_bak):
            return piece
    
    return None
            
            

def get_winner(matrix, must_connect):
    n = len(matrix)
    red_wins = False
    blue_wins = False
    
    for i in xrange(n):
        for j in xrange(n):
            piece = get_winner_at(i, j, matrix, must_connect)
            
            if piece is not None:
                if piece == "R":
                    red_wins = True
                else:
                    blue_wins = True
    
    if red_wins and blue_wins:
        return "Both"
    elif red_wins:
        return "Red"
    elif blue_wins:
        return "Blue"
    else:
        return "Neither"
    

def do_case(case):
    params = line_to_ints(case[0])
    size = params[0]
    must_connect = params[1]
    return get_winner(do_gravity([row.strip() for row in case[1:]]), must_connect)

if __name__ == "__main__":
    lines = open(sys.argv[1], "r").readlines()
    case_num = 0
    i = 1
    
    while i < len(lines):
        case_num += 1
        case_len = int(lines[i].split()[0])
        print("Case #%d: %s" % (case_num, do_case(lines[i:i+case_len+1])))
        i += case_len + 1
