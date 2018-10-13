'''
Created on May 20, 2011

@author: mk
'''


def gcd(x, y):
    while True:
        if x==y:
            return x
        if x>y:
            x = x-y
        if x<y:
            y = y-x

def solveCase(index, max_games_played_today, percent_today, percent_ever):
    result = True
    if percent_today > 0 and percent_ever == 0:
        result = False
    elif percent_today < 100 and percent_ever == 100:
        result = False
    else:
        if percent_today > 0:
            min_games_played_today = 100 / gcd(percent_today, 100)
            if min_games_played_today > max_games_played_today:
                result = False
        
    return "Case #{0}: {1}\n".format(index, result and "Possible" or "Broken")
    

def solve(fin, fout):
    cases = int(fin.readline())
    for index in range(cases):
        # load case
        max_played_today, percent_today, percent_ever = map(int, fin.readline().split())
        fout.write(solveCase(index+1, max_played_today, percent_today, percent_ever))


def testSolve():
    from StringIO import StringIO
    input = StringIO("""6
1 100 50
10 10 100
9 80 56""")
    solve(input, sys.stdout)

if __name__ == '__main__':
    import sys
    #testSolve()
    solve(sys.stdin, sys.stdout)
