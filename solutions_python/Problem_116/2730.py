

def input_handler():
    number_of_inputs = int(input())
    games = {}
    for i in range(number_of_inputs):
        games[i] = []
        for j in range(4):
            raw = input()
            raw = [ i for i in raw]
            games[i].append(raw)
        input() # this is to remove empty line
    return games

def transform_list(l):
    new_l = []
    for c in range(len(l[0])):
        tmp_l = []
        for r in range(len(l)):
            tmp_l.append(l[r][c])
        new_l.append(tmp_l)
    return new_l


def who_won_r(game):
    #scan raw
    for r in game:
        count_O = count_X = 0
        for c in r:
            if c == 'X': count_X += 1
            if c == 'O': count_O += 1

        if count_X == 4 or (count_X == 3 and 'T' in r):
            return 'X'
        elif count_O == 4 or (count_O == 3 and 'T' in r):
            return 'O'

    # check columns
def who_won_c(game):
    return who_won_r(transform_list(game))

    #diagonal
def who_won_dig(game):
    count_X = 0
    count_O = 0
    count_X2 = 0
    count_O2 = 0
    diag_l = []
    diag_l2 = []

    for i in range(len(game)):
        diag_l.append(game[i][i])

    for i in range(len(game)):
        diag_l2.append(game[i][abs(3-i)])

    for c in diag_l:
        if c == 'X': count_X += 1
        if c == 'O': count_O += 1

    for c in diag_l2:
        if c == 'X': count_X2 += 1
        if c == 'O': count_O2 += 1


    if count_X == 4 or (count_X == 3 and 'T' in diag_l) or (count_X2 == 3 and 'T' in diag_l2):
        return 'X'
    elif count_O == 4 or (count_O == 3 and 'T' in diag_l) or (count_O2 == 3 and 'T' in diag_l2):
        return 'O'

def count_dots(game):
    dots = 0
    for r in game:
        for c in r:
            if c == '.': dots += 1
    return dots

def who_won(game):
    who = who_won_r(game) or who_won_c(game) or who_won_dig(game)
    if who == 'X': who = 'X won'
    if who == 'O': who = 'O won'
    if (not who) and count_dots(game) == 0: who = 'Draw'
    if (not who) and count_dots(game) > 0: who = 'Game has not completed'

    return who

if __name__ == '__main__':
    game = input_handler()
    for i in game:
        print("Case #{}: {}".format(i+1, who_won(game[i])))
