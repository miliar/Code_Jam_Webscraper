def check_group(group):
    mapping = {'X': 1, 'O': -1, 'T': 0, '.': 10}
    sum=0
    for element in group:
        sum += mapping[element]
    if sum > 6:
        return (2, "Game has not completed")
    elif sum == 3 or sum == 4:
        return (0, "X won")                 
    elif sum == -3 or sum == -4: 
        return (0, "O won")
    else:
        return (1, "Draw") 

def read_input(filename):
    f = open(filename)
    tests = int(f.readline())

    for test in xrange(tests):
        game = []
        combinations = []
        for row in xrange(4):
            game.append(list(f.readline()[:-1]))
        f.readline()
        for ii in xrange(4):
            row = []
            col = []
            for jj in xrange(4):
                row.append(game[ii][jj])
                col.append(game[jj][ii])
            combinations.append(row)
            combinations.append(col)
        combinations.append([game[0][0], game[1][1], game[2][2], game[3][3]])
        combinations.append([game[0][3], game[1][2], game[2][1], game[3][0]])
        yield(test, combinations)

myinput = read_input('A-large.in')
output_file = open('Tic-Tac-Toe-Tomek.out', "w")

for i in myinput:
    not_completed = False
    won = False
    for combination in i[1]: 
        result = check_group(combination)
        draw = result[0]
        if result[0] == 0:
            output_file.write("Case #%d: %s\n" % (i[0]+1, result[1]))
            won = True
            not_completed = False
            break
        elif result[0] == 2:
            not_completed = True 
    if not_completed:
        output_file.write("Case #%d: Game has not completed\n" % (i[0]+1))
    elif not won:
        output_file.write("Case #%d: Draw\n" % (i[0]+1))

output_file.close()
