INPUT = {
    'data': ('string', 'linearray')
}

TEST = ('''\
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
''','''\
Case #1: 6
Case #2: 100
Case #3: 4
''')
def main(data):
    seq = zip(data[1::2], map(int,data[2::2]))
    pos = {'O':1,'B': 1} # initial positions
    moves = {'O': 0, 'B': 0}
    
    for (bot, goal) in seq:
        other_bot = 'O' if bot == 'B' else 'B'
        add_moves = abs(pos[bot] - goal) + 1
        total_moves = moves[bot] + add_moves
        other_bot_moves = moves[other_bot]
        if total_moves > other_bot_moves:
            moves[bot] = total_moves
        else:
            moves[bot] = other_bot_moves + 1
        pos[bot] = goal
    return moves[seq[-1][0]]