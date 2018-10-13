def rotate_board(board):
    mass = [ filter(None, row) for row in board ]
    padded = [ [0]*(len(board)-len(row))+row for row in mass ]
    return [ [ padded[col][row] for col in range(len(board))[::-1] ] for row in range(len(board)) ]

             
def parse_board(s):
    x = {".":0, "R":1, "B":2}
    return [ [ x[c] for c in line.strip() ] for line in s ]
    

def print_board(b):
    x = ['.', 'R', 'B']
    return "\n".join("".join(map(lambda y:x[y], line)) for line in b)


def finder(b, k):
    from gridsearch import find_combo
    red = 1
    blue = 2
    #print print_board(b)
    b = rotate_board(b)
    #print print_board(b)
    #print k
    red, blue = find_combo(b, [red]*k, 0), find_combo(b, [blue]*k, 0)
    if red >= 0 and blue >= 0:
        return "Both"
    elif red < 0 and blue < 0:
        return "Neither"
    else:
        return "Red" if red >= 0 else "Blue"
        

def main(s):
    lines = s.split("\n")
    cases = int(lines[0])
    n = 1
    for i in range(cases):
        size, win = map(int, lines[n].strip().split(" "))
        b = parse_board(lines[n+1:n+size+1])
        n+=size+1
        print "Case #%d: %s" % (i+1, finder(b, win))


