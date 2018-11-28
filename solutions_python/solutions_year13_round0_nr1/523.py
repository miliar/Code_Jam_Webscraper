from collections import defaultdict


map_size = 4


def represent_map(map):
    map = map.split('\n')
    dct = defaultdict(list)
    for x in xrange(map_size):
        for y in xrange(map_size):
            if map[x][y] == 'X':
                dct['X'].append((x, y))
            elif map[x][y] == 'O':
                dct['O'].append((x, y))
            elif map[x][y] == 'T':
                dct['X'].append((x, y))
                dct['O'].append((x, y))
            else:
                dct['empty'].append((x, y))
    return dct


def horizontal_win(lst):
    dct = defaultdict(list)
    for x, y in lst:
        dct[x].append(y)

    if any(range(min(x), max(x) + 1) == x and len(x) == 4
           for x in dct.itervalues()):
        return True
    return False


def vertical_win(lst):
    dct = defaultdict(list)
    for x, y in lst:
        dct[y].append(x)

    if any(range(min(x), max(x) + 1) == x and len(x) == 4
           for x in dct.itervalues()):
        return True
    return False


def diag_win(lst):
    if set([(0, 0), (1, 1), (2, 2), (3, 3)]) <= set(lst):
        return True
    elif set([(0, 3), (1, 2), (2, 1), (3, 0)]) <= set(lst):
        return True
    return False


def judge_game(game_dct):
    if len(game_dct['X']) < 4 and len(game_dct['O']) < 4:
        return 'Game has not completed'

    if horizontal_win(game_dct['X']) or vertical_win(game_dct['X']) or\
            diag_win(game_dct['X']):
        return 'X won'
    elif horizontal_win(game_dct['O']) or vertical_win(game_dct['O']) or\
            diag_win(game_dct['O']):
        return 'O won'
    elif not game_dct['empty']:
        return 'Draw'
    else:
        return 'Game has not completed'


input_file = "/Users/gerrrr/Downloads/A-large.in"
text = ''
with open(input_file) as f:
    f.readline()
    text = f.read().strip()

maps = text.split('\n\n')
game_dcts = map(represent_map, maps)
results = map(judge_game, game_dcts)
for i, r in enumerate(results):
    print 'Case #%s: %s' % (i + 1, r)
