import pprint
import string
import sys

def read_board(in_fd):
    board = []
    for i in range(4):
        board.append(list(in_fd.readline().strip()))
    in_fd.readline()
    return board

def containsOnly(li, chars):
    for c in li:
        if not c in chars:
            return False
    return True

def main(in_fd, out_fd):
    n = int(in_fd.readline())
    for i in range(n):
        b = read_board(in_fd)

        def checkWon(c):
            for l in b:
                if containsOnly(l, [c, 'T']):
                    return True
            
            for col in range(4):
                if containsOnly([b[0][col], b[1][col], b[2][col], b[3][col]], [c, 'T']):
                    return True
            if containsOnly([b[0][0], b[1][1], b[2][2], b[3][3]], [c, 'T']):
                return True
            if containsOnly([b[0][3], b[1][2], b[2][1], b[3][0]], [c, 'T']):
                return True
            return False

        def game_not_finished():
            for l in b:
                if '.' in l:
                    return True
            return False

        if checkWon('X'):
            write_output(out_fd, i, "X won")
        elif checkWon('O'):
            write_output(out_fd, i, "O won")
        elif game_not_finished():
            write_output(out_fd, i, "Game has not completed")
        else:
            write_output(out_fd, i, "Draw")

def write_output(out_fd, i, output):
    out_fd.write('Case #{0}: {1}\n'.format(i + 1, output))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Need file name"
        sys.exit(1)
    in_name = sys.argv[1]
    out_name = string.replace(in_name, ".in", ".out")
    with open(in_name) as in_fd:
        with open(out_name, 'w') as out_fd:
            main(in_fd, out_fd)
