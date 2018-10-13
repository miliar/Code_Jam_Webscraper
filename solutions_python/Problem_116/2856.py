import sys


def get_simb(simbol_str):
    simb = simbol_str
    if simb == 'T':
        simb = 'XO'
    return simb

def scan_board(board):
    unfinished = None
    winner = None
    for i in range(4):
        for j in range(4):
            simb = get_simb(board[i][j])
            if simb == '.': #there's at least one '.'
                unfinished = True
                continue

            for direction in ['E','S','SE','SO']:
                winner = None
                if direction == 'E':
                    if j > 0:
                        continue
                    else:
                        for k in range(1,4):
                            winner = None
                            new_simb = get_simb(board[i][j+k])
                            if simb in new_simb:
                                winner = simb
                            elif new_simb in simb:
                                simb = new_simb
                                winner = simb
                            if not winner:
                                break
                        if winner:
                            return winner, unfinished

                elif direction == 'S':
                    if i > 0:
                        continue
                    else:
                        for k in range(1,4):
                            winner = None
                            new_simb = get_simb(board[i+k][j])
                            if simb in new_simb:
                                winner = simb
                            elif new_simb in simb:
                                simb = new_simb
                                winner = simb
                            if not winner:
                                break
                        if winner:
                            return winner, unfinished
                            
                elif direction == 'SE':
                    if i > 0 or j > 0:
                        continue
                    else:
                        for k in range(1,4):
                            winner = None
                            new_simb = get_simb(board[i+k][j+k])
                            if simb in new_simb:
                                winner = simb
                            elif new_simb in simb:
                                simb = new_simb
                                winner = simb
                            if not winner:
                                break
                        if winner:
                            return winner, unfinished

                elif direction == 'SO':
                    if i > 0 or j < 3:
                        continue
                    else:
                        for k in range(1,4):
                            winner = None
                            new_simb = get_simb(board[i+k][j-k])
                            if simb in new_simb:
                                winner = simb
                            elif new_simb in simb:
                                simb = new_simb
                                winner = simb
                            if not winner:
                                break
                        if winner:
                            return winner, unfinished

    return winner, unfinished

to_result_string = {'X': 'X won', 'O': 'O won'}

def main():
    T = int(sys.stdin.readline().strip())
    for case in range(T):
        board = list()
        for l in range(4):
            line = sys.stdin.readline().strip()
            board.append(line)
        winner, unfinished = scan_board(board)
        if winner:
            res = to_result_string[winner]
        else:
            if unfinished:
                res = 'Game has not completed'
            else:
                res = 'Draw'

        sys.stdout.write('Case #%d: %s\n' % (case+1, res))
        sys.stdin.readline() #skip empty line


if __name__ == '__main__':
    main()
