
import csv

def check(board):
    candidate = []
    for row in board:
        candidate.append(row)
    for inx in range(4):
        candidate.append([board[i][inx] for i in range(4)])
    candidate.append([board[i][i] for i in range(4)])
    candidate.append([board[3-i][i] for i in range(4)])
    
    for candy in candidate:
        candy = set(candy)
        print(candy)
        if candy == {'X'} or candy == {'X', 'T'}:
            return 'X won'
        elif candy == {'O'} or candy == {'O', 'T'}:
            return 'O won'
            
    for candy in candidate:
        if '.' in candy:
            return 'Game has not completed'
    else:
        return 'Draw'

if __name__ == '__main__':
    data_set = []
    with open('A-small-attempt0.in') as f:
        data = []
        for (inx, line) in enumerate(f):
            # print(line)
            if inx == 0:
                continue
            elif len(line) < 2:
                data_set.append(data)
                data = []
            else:
                data.append(list(line)[:4])
        #print(data)
    #print(data_set)
    with open('tictac', 'w') as g:
        for (inx, data) in enumerate(data_set):
            print data
            g.write('Case #{0}: {1}\n'.format(inx + 1, check(data)))
