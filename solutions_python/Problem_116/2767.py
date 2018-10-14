r = open('A-small-attempt1.in')
f = open('a.out', 'w')

T = int(r.readline())
case = 1
while case <= T:
    output_text = 'Case #'+str(case)+': '
    case += 1
    diag1 = []
    diag2 = []
    cols = [[], [], [], []]
    rows = [[], [], [], []]
    for i in range(4):
        line = r.readline()
        for j in range(4):
            char = line[j]
            rows[i].append(char)
            cols[j].append(char)
            if i == j:
                diag1.append(char)
            if i+j == 3:
                diag2.append(char)
    every = cols + rows + [diag1] + [diag2]

    game_over = False
    open_line = False
    for line in every:
        o_seen = False
        x_seen = False
        dot_seen = False
        for i in range(4):
            char = line[i]
            if char == '.': 
                dot_seen = True
            elif char == 'X': 
                x_seen = True
            elif char == 'O':
                o_seen = True
        if not dot_seen:
            if x_seen and not o_seen:
                output_text += 'X won'
                game_over = True
                break
            elif o_seen and not x_seen:
                output_text += 'O won'
                game_over = True
                break
        if o_seen and not x_seen:
            open_line = True
        elif x_seen and not o_seen:
            open_line = True
        elif not o_seen and not x_seen:
            open_line = True

    if not game_over:
        if open_line:
            output_text += 'Game has not completed'
        else:
            output_text += 'Draw'
    r.readline()
    f.write(output_text)
    f.write('\n')
