import re

class game:
    def __init__(self):
        pass
    def __str__(self):
        return 'choice1:{}\nchoice2:{}cards1:{}\ncards2:{}'.format(self.choice1,
                self.choice2, self.cards1, self.cards2)

def read_file(filename):
    f = open(filename, 'r')
    lines = []
    for line in f:
       lines.append(re.findall(r'\w+', line))
    f.close()
    numTests = int(lines[0][0])
    games = []
    for i in range(0, numTests):
        j = i * 10 + 1
        choice1 = int(lines[j][0])
        choice2 = int(lines[j+5][0])
        cards1 = lines[j+1:j+5]
        cards2 = lines[j+6:j+10]
        g = game()
        g.choice1 = choice1 - 1
        g.choice2 = choice2 - 1
        g.cards1 = cards1
        g.cards2 = cards2
        games.append(g)
    return games

# pos : set * row : int * cards : int list list -> set 
def find_card(pos, row, cards):
    return set(cards[row]) & pos

# game : game -> string 
def solve_game(game):
    soln = find_card(set(map(str, range(1,17))), game.choice1, game.cards1)
    soln = find_card(soln, game.choice2, game.cards2)
    if len(soln) == 0:
        return 'Volunteer cheated!'
    elif len(soln) == 1:
        return str(soln.pop())
    return 'Bad magician!'


def generate_output(filename):
    games = read_file(filename)
    solutions = list(map(solve_game, games))
    f = open('out.txt', 'w')
    for i in range(len(solutions)):
        f.write('Case #{}: {}\n'.format(i+1, solutions[i]))




