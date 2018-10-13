import sys
winning_states = [set(('X','T')),set(('O','T')),set('X'),set('O')]
output = ''

def check_line(line):
    if set(line) in winning_states:
        if 'X' in line:
            return 'X won'
        else:
            return 'O won'
    return ''


def main():
    global output
    with open(sys.argv[1]) as input:
        with open(sys.argv[2],'w') as out:
            cases = int(input.readline().strip())
            for case in range(1,cases+1):
                board = []
                not_finished = False
                output = ''
                for row in range(0,4):
                    board.append(input.readline().rstrip('\n'))
                for row in board:
                    output = check_line(row)
                    if output != '':
                        break
                    if '.' in row:
                        not_finished = True
                if output == '':
                    for column in range(0,4):
                        c =[board[0][column],board[1][column],board[2][column],board[3][column]] 
                        output = check_line(c)
                        if output != '':
                            break
                    if output == '':
                        leading_diag = [board[0][0],board[1][1],board[2][2],board[3][3]]
                        output = check_line(leading_diag)
                        if output =='':
                            other_diag = [board[0][3],board[1][2],board[2][1],board[3][0]]
                            output = check_line(other_diag)
                    if output == '':
                        if not_finished:
                            output = 'Game has not completed'
                        else:
                            output = 'Draw'
                input.readline()
                txt = 'Case #{}: {}\n'.format(case,output)
                print(txt)
                out.write(txt)
if __name__=='__main__':
    main()
