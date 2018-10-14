# Python version 2.7
import sys

size = 4

def oneCase():
    game = []
    for i in range(size):
        game.append(sys.stdin.readline())
    
    mX = map(lambda line: map(lambda c: 1 if c=='X' or c=='T' else 0, line), game)
    mO = map(lambda line: map(lambda c: 1 if c=='O' or c=='T' else 0, line), game)
    haveEmpty = any(map(lambda line: any(map(lambda c: c=='.', line)), game))
    
    sumX = []
    sumO = []
    for i in range(size):
        sumX.append(sum(mX[i]))
        sumO.append(sum(mO[i]))
        sumX.append(sum(map(lambda x: x[i], mX)))
        sumO.append(sum(map(lambda x: x[i], mO)))
    
    sumX.append(sum(map(lambda i: mX[i][i], range(size))))
    sumO.append(sum(map(lambda i: mO[i][i], range(size))))
    sumX.append(sum(map(lambda i: mX[i][size-i-1], range(size))))
    sumO.append(sum(map(lambda i: mO[i][size-i-1], range(size))))
    if max(sumX) == size: return "X won"
    if max(sumO) == size: return "O won"
    return "Game has not completed" if haveEmpty else "Draw"    
    
    

cases = int(sys.stdin.readline())
for i in range(cases):
    print "Case #" + str(i+1) + ": " + oneCase()
    sys.stdin.readline()
    