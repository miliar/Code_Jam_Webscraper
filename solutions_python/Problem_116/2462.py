from sys import stdin
from compiler.ast import flatten

def status():
    fours = [list(stdin.readline()) for i in range(4)]
    fours.extend(zip(*fours))
    fours.append([fours[i][i] for i in range(4)])
    fours.append([fours[i][3-i] for i in range(4)])
    for f in fours:
	if abs(f.count('X')-f.count('O'))+f.count('T')==4:
	    return 'X won' if f.count('X')>0 else 'O won'
    return 'Game has not completed' if '.' in flatten(fours) else 'Draw'


for c in range(int(stdin.readline())):
    print 'Case #'+str(c+1)+':', status()
    stdin.readline()
