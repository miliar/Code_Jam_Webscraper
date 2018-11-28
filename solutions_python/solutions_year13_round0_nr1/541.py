lines = open('data.txt').read()

lines = lines.split()[1:]
n = 4
for i in range(0, len(lines), n):
    case_num = i/4 + 1
    game_lines = '\n'.join(lines[i:i + n]).replace('T', '1')
    x_game_lines = game_lines.replace('X', '1').replace('O', '0').replace('.', '0').split()
    o_game_lines = game_lines.replace('O', '1').replace('X', '0').replace('.', '0').split()

    # check x
    x_hor_res = set([sum([int(x) for x in line]) for line in x_game_lines])
    x_ver_res = set([sum(int(x) for x in line) for line in zip(*[line for line in x_game_lines])])
    x_diag_res = sum([int(line[i]) for i, line in enumerate(x_game_lines)])
    x_diag_res1 = sum([int(line[-1 - i]) for i, line in enumerate(x_game_lines)])
    if 4 in x_hor_res or 4 in x_ver_res or x_diag_res == 4 or x_diag_res1 == 4:
        print 'Case #{0}:'.format(case_num), 'X won'
        continue

    # check O
    o_hor_res = set([sum([int(x) for x in line]) for line in o_game_lines])
    o_ver_res = set([sum(int(x) for x in line) for line in zip(*[line for line in o_game_lines])])
    o_diag_res = sum([int(line[i]) for i, line in enumerate(o_game_lines)])
    o_diag_res1 = sum([int(line[-1 - i]) for i, line in enumerate(o_game_lines)])
    if 4 in o_hor_res or 4 in o_ver_res or o_diag_res == 4 or o_diag_res1 == 4:
        print 'Case #{0}:'.format(case_num), 'O won'
        continue

    if '.' in game_lines:
        print 'Case #{0}:'.format(case_num), "Game has not completed"
    else:
        print 'Case #{0}:'.format(case_num), 'Draw'


