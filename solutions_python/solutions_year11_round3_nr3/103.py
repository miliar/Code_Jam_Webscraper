INPUT = {
    'config': ('int', 'linearray'),
    'players': ('int', 'linearray')
}

INPUT_ORDER = ['config', 'players']

TEST = ('''\
2
3 2 100
3 5 7
4 8 16
1 20 5 2
''','''\
Case #1: NO
Case #2: 10
''')

def main(config, players):
    N, L, H = config
    if L == 1: return 1
    
    def test(x,y):
        return (x % y == 0) or (y % x == 0)
    
    def testAll(x):
        for y in players:
            if not test(x,y):
                return False
        return True
        
    for x in range(L, H+1):
        if testAll(x):
            return x
    
    return 'NO'