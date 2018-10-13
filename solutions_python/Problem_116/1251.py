from parser import parse, maplist

parse_string = \
"""
<int t>
$t{
<str a>
<str b>
<str c>
<str d>
<str _>
>>> solve(tuple($a), tuple($b), tuple($c), tuple($d))
}
>>> print_cases(list(%t))
"""

def solve(a, b, c, d):
    states = [a, b, c, d] + list(zip(a, b, c, d))
    states.append((a[0], b[1], c[2], d[3]))
    states.append((a[3], b[2], c[1], d[0]))
    wins = [check_win(i) for i in states]
    if 'X' in wins:
        return 'X won'
    elif 'O' in wins:
        return 'O won'
    elif '.' in a + b + c + d:
        return 'Game has not completed'
    else:
        return 'Draw'

def check_win(l):
    if '.' in l:
        return None
    if ('X' in l) and ('O' not in l):
        return 'X'
    if ('O' in l) and ('X' not in l):
        return 'O'
    return None
        
    
def print_cases(l):
    for i, n in enumerate(l):
        print("Case #{0}: {1}".format(i + 1, n))

if __name__ == '__main__':
    parse(parse_string, globals())

