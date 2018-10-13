import sys
import StringIO
import re

def check_game(lawn):
    row_max = [max(x) for x in lawn]
    cols = [[lawn[i][j] for i in range(len(lawn))] for j in range(len(lawn[0]))]
    col_max = [max(x) for x in cols]
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            val = lawn[i][j]
            if val != row_max[i] and val != col_max[j]:
                return "NO"
    return "YES"
        

def read_game():
    size = re.split(" ",sys.stdin.readline())
    x,y = int(size[1]), int(size[0])    
    lawn = []
    for i in range(y):
        line = sys.stdin.readline()
        cuts = [int(x.strip()) for x in re.split(" ",line)]
        lawn.append(cuts)
    return lawn

testcase = sys.stdin.readline()
for i in range(int(testcase.strip())):
	lawnstate = read_game()
	outline = "Case #%d: %s" % (i+1, check_game(lawnstate))
	print outline