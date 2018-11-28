# coding: utf8

def scan():
    while True:
        for w in input().split():
            yield w

words = scan()

def scans(num=-1):
    return (next(words) for i in range(num)) if num >= 0 else next(words)

def scani(num=-1):
    return (int(value) for value in scans(num)) if num >= 0 else int(scans())

def scanf(num=-1):
    return (float(value) for value in scans(num)) if num >= 0 else float(scans())

#------------------------------------------------------------------------------
search_ways = ([(i, 4) for i in range(0, 4, 1)] + 
               [(i, 1) for i in range(0, 16, 4)] +
               [(0, 5), (3, 3)])

for case in range(1, scani() + 1):
    board = ''.join(scans() for i in range(4))
    def judge(s, o):
        res = [False, False] # exist X, exist O
        for i in range(4):
            ch = board[s]
            if ch == '.': return (False, False)
            elif ch == 'X': res[0] = True
            elif ch == 'O': res[1] = True
            if res[0] and res[1]: return res
            s += o
        return res
    completed = True
    res = None
    for way in search_ways:
        exist_x, exist_o = judge(*way)
        if exist_x == exist_o:
            if not exist_x: completed = False
        elif exist_x:
            res = 'X won'
            break
        else:
            res = 'O won'
            break
    if not res: res = 'Draw' if completed else 'Game has not completed'
    print("Case #{0}: {1}".format(case, res))
