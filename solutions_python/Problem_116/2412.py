def print_table(table):
    for row in table:
        print(' '.join(row))

# Get input to tables variable

input_file_name = 'A-large.in.txt'
input = [line.strip() for line in open(input_file_name)]
input.append('')
it = iter(input)
tables = []

for i in range(int(it.next())):
    table_size = 4
    table = []
    for j in range(table_size):
        table.append(list(it.next()))
    it.next()
    tables.append(table)
        
# logic

def get_rows(t):
    return t

def get_columns(t):
    columns = []
    for i in range(len(t)):
        columns.append([row[i] for row in t])
    return columns

def get_diag(t):
    diags = []
    diags.append([v[i] for i, v in enumerate(t)])
    diags.append([v[len(t) - i -1] for i, v in enumerate(t)])
    return diags

def eval_game(game):
    no_more_move = True
    winner = ''
    for g in game:
        if '.' in g:
            no_more_move = False
            continue
        if 'X' in g and 'O' in g:
            continue
        s = set(g)
        if len(s) <= 2 :
            if 'T' in s:
                s.remove('T')
            if 'X' in s:
                winner = 'X'
            if 'O' in s:
                winner = 'O'
            break
    result = ''
    if winner:
        result = "%s won" % winner
    elif no_more_move:
        result = "Draw"
    else:
        result = "Game has not completed"
    return result

for c,t in enumerate(tables):   
    pos = []
    pos.extend(get_rows(t))
    pos.extend(get_columns(t))
    pos.extend(get_diag(t))
    result = eval_game(pos)
    print("Case #%i: %s" % (c + 1, result))

