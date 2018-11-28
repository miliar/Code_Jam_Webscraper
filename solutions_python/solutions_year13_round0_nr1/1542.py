def same_player(p1, p2):
    return (p1 == 'T' or p2 == 'T' or p1 == p2) and p1 != '.' and p2 != '.'

def game_full(game):
   for line in game:
       for char in line:
           if char == '.':
               return False
   return True

def read_game():
    game = list()
    for i in xrange(4):
        game.append(raw_input())
    raw_input() # read the empty line
    return game
    
def game_analyse(game):
    winner = None
    # first check line
    for x in xrange(4):
        if same_player(game[x][0], game[x][1]) and same_player(game[x][1], game[x][2]) and same_player(game[x][2], game[x][3]):
           winner = game[x][0] if game[x][0] != 'T' else game[x][1]
           break
    
    # then check column
    if winner is None:
        for y in xrange(4):
            if same_player(game[0][y], game[1][y]) and same_player(game[1][y], game[2][y]) and same_player(game[2][y], game[3][y]):
               winner = game[0][y] if game[0][y] != 'T' else game[1][y]
               break
    # end finnaly check column
    if winner is None:
        if same_player(game[0][0], game[1][1]) and same_player(game[1][1], game[2][2]) and same_player(game[2][2], game[3][3]):
           winner = game[0][0] if game[0][0] != 'T' else game[1][1]

        if same_player(game[0][3], game[1][2]) and same_player(game[1][2], game[2][1]) and same_player(game[2][1], game[3][0]):
           winner = game[0][3] if game[0][3] != 'T' else game[1][2]
       
    
    if winner is None:
      if game_full(game):
          return 'Draw'
      else:
          return 'Game has not completed'
    else:
        return winner + ' won'

n_test_case = input()
for i in xrange(1, n_test_case+1):
    print 'Case #%d: ' % (i) + game_analyse(read_game())
