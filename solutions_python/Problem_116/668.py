def check_diagonal(board_state, player_state):
    return not all((
        set(board_state[i][i] for i in xrange(4)) - player_state,
        set(board_state[3 - i][i] for i in xrange(4)) - player_state
    ))


def check_for_winner(board_state, player):
    player_state = {'T', player}
    for line in map(set, board_state):
        if not line - player_state:
            return True
    if check_diagonal(board_state, player_state):
        return True

    return any(
        not set(board_state[i][j] for i in xrange(4)) - player_state for j in xrange(4)
    )


def inputer(file_name):
    with open(file_name, 'r') as in_file:
        cases = int(in_file.readline())
        for case_number in xrange(cases):
            board_state = tuple(in_file.readline()[:-1] for x in xrange(4))
            yield board_state, case_number
            in_file.readline()


def solve(file_name, out_file_name):
    out_file = open(out_file_name, 'w')
    for board_state, case in inputer(file_name):
        out_file.write('Case #%d: ' % (case + 1))
        winner = None

        for player in ('X', 'O'):
            if check_for_winner(board_state, player):
                winner = player
                break
        if winner:
            out_file.write('%s won\n' % winner)
            continue

        if any(filter(lambda x: '.' in x, board_state)):
            out_file.write('Game has not completed\n')
        else:
            out_file.write('Draw\n')
    out_file.close()


if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    solve(file_name, out_file_name)
