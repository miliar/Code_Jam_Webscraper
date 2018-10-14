def solve(cases):
    count_case = 1

    for case in cases:

        lines_h = [ case[i][0] for i in range(4)]
        lines_v = [ ''.join([lines_h[j][i] for j in range(4)]) for i in range(4)]
        diag = [''.join([ lines_h[i][i] for i in range(4)]), ''.join([ lines_h[3-i][i] for i in range(4)])] 

        has_winner, winner = search_winner(lines_h + lines_v + diag)
        if has_winner:
            print 'Case #{}: {} won'.format(count_case, winner)
        elif has_empty_squares(case):
            print 'Case #{}: {}'.format(count_case, 'Game has not completed')
        else:
            print 'Case #{}: {}'.format(count_case,'Draw')
        count_case += 1
            

def has_empty_squares(case):
    for tic_tac_line in case:
        line = ''.join(tic_tac_line)
        if line.find('.') != -1:
            return True
        return False


def search_winner(game):
    for line in game:
        if line.count('O') == 4 or line.count('O') == 3 and line.count('T') == 1:
            return (True,'O')
        elif line.count('X') == 4 or line.count('X') == 3 and line.count('T') == 1:
            return (True,'X')

    return (False, '')


if __name__ == "__main__":
    from google_input_parser import InputParser
    cases = InputParser.Parser('A-small-attempt0.in').get_chunks()
    solve(cases)
