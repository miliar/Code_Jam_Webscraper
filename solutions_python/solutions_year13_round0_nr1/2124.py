
lines = open('A-large.in').read().splitlines()

num_cases = int(lines[0])

wining_seq = []

output = []

for i in range(num_cases):
    start = i*5 + 1
    rows = lines[start: start+4]

    cases =[rows[0][0] + rows[0][1] + rows[0][2] + rows[0][3],
            rows[1][0] + rows[1][1] + rows[1][2] + rows[1][3],
            rows[2][0] + rows[2][1] + rows[2][2] + rows[2][3],
            rows[3][0] + rows[3][1] + rows[3][2] + rows[3][3],
            rows[0][0] + rows[1][0] + rows[2][0] + rows[3][0],
            rows[0][1] + rows[1][1] + rows[2][1] + rows[3][1],
            rows[0][2] + rows[1][2] + rows[2][2] + rows[3][2],
            rows[0][3] + rows[1][3] + rows[2][3] + rows[3][3],
            rows[0][0] + rows[1][1] + rows[2][2] + rows[3][3],
            rows[3][0] + rows[2][1] + rows[1][2] + rows[0][3]]

    won = False
    for case in cases:
        if case.replace('T', 'X') == 'XXXX':
            won = True
            output.append('X won')
            break;
        if case.replace('T', 'O') == 'OOOO':
            won = True
            output.append('O won')
            break;

    if not won:
        if ''.join(rows).find('.') == -1:
            output.append('Draw')
        else:
            output.append('Game has not completed')

o_file = open('A-large.out', 'w+')
for i in range(num_cases):
    o_file.write("Case #%s: %s\n" % ( str(i+1), output[i] ))