
def game(lines):
    game_complete = True
    #waagerecht
    for line in lines:
        if '.' in line:
            game_complete = False
        # X winning
        x_winning = True
        for letter in line:
            if letter in 'XT':
                continue
            x_winning = False
            break
        if x_winning:
            return 'X won'
        # O winning
        o_winning = True
        for letter in line:
            #print letter
            if letter in 'OT':
                #print letter in 'OT'
                continue
            o_winning = False
            break
        if o_winning:
            return 'O won'

    # senkrecht
    for i in xrange(4):
        x_winning = True
        o_winning = True
        for j in xrange(4):
            if lines[j][i] not in 'XT':
                x_winning = False
            if lines[j][i] not in 'OT':
                o_winning = False
        if x_winning:
            return 'X won'
        if o_winning:
            return 'O won'

    # diagonal
    x_winning = False
    o_winning = False
    if lines[0][0] in 'XT' and lines[1][1] in 'XT' and \
       lines[2][2] in 'XT' and lines[3][3] in 'XT' or \
       (lines[0][3] in 'XT' and lines[1][2] in 'XT' and \
        lines[2][1] in 'XT' and lines[3][0] in 'XT'):
        x_winning = True
    if lines[0][0] in 'OT' and lines[1][1] in 'OT' and \
       lines[2][2] in 'OT' and lines[3][3] in 'OT' or \
       (lines[0][3] in 'OT' and lines[1][2] in 'OT' and \
        lines[2][1] in 'OT' and lines[3][0] in 'OT'):
        o_winning = True
    if x_winning:
        return 'X won'
    if o_winning:
        return 'O won'

    if not game_complete:
        return 'Game has not completed'
    return 'Draw'
            

def main():
    in_put = []
    file = open('A-large.in')
    for line in file:
        in_put.append(line.strip())
    in_put.pop(0)
    while '' in in_put:
        in_put.remove('') 

    result = []
    for i in xrange(0, len(in_put)-1, 4):
        result.append(game(in_put[i:i+4]))

    output = open('output.txt', 'w')
    for i, n in enumerate(result):
        output.write("Case #" + str((i+1))+ ': ' + n + '\n') 
    return result


print main()
