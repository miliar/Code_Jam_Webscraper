import itertools
import sys

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

def parse_player_deck(line):
    return [float(x) for x in line.split()]

def parse_case(lines):
    return {
        'player1': parse_player_deck(lines[1]),
        'player2': parse_player_deck(lines[2])
    }

def parse_file(in_file):
    return (parse_case(case) for case in grouper(3, in_file.readlines()[1:]))

def losers_until_winner(A, target):
    losers = 0
    while (A):
            if A.pop() > target:
                    break
            losers = losers + 1
    return losers

def W(player1, player2):
    player1.sort()
    player2.sort(reverse=True)
    return sum(losers_until_winner(player2, x) for x in player1)

def D(player1, player2):
    p1_max = max(player1)
    p2_min = min(player2)
    N = len(player1)
    p1_too_low = len(filter(lambda x: x < p2_min, player1))
    p2_too_high = len(filter(lambda x: x > p1_max, player2))
    return N - max(p1_too_low, p2_too_high)

def run_case(n, input_data):
    t = len(input_data['player1'])
    #d = D(input_data['player1'], input_data['player2'])
    w = W(input_data['player1'][:], input_data['player2'][:])
    d = t - W(input_data['player2'][:], input_data['player1'][:])
    print "Case #{0}: {1} {2}".format(n, d, w)

if len(sys.argv) < 2:
    exit();
    
with open(sys.argv[1], 'r') as in_file:
    for n, case in enumerate(parse_file(in_file), start=1):
        run_case(n, case)
