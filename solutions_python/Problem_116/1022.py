# GOOGLE CODE JAM 2013
# PROBLEM 1 Tic-Tac-Toe-Tomek
import sys

def checkWinner(l):
    dots = 0
    for line in l:
        if line.count('X') + line.count('T') == 4: return 'X'
        if line.count('O') + line.count('T') == 4: return 'O'
        dots += line.count('.')
    if dots > 0: return 'U'
    return 'D'
        
def run():
    t = int(raw_input())
    for x in range(t):
        data = []
        for y in range(4):
            data.append(raw_input())
        for i in range(4):
            s = ''
            for j in range(4):
                s = s + data[j][i]
            data.append(s)
        s1 = ''
        s2 = ''
        for i in range(4):
            s1 = s1 + data[i][i]
            s2 = s2 + data[i][3-i]
        data.append(s1)
        data.append(s2)
        winner = checkWinner(data)
        if winner == 'X':
            print 'Case #%d: X won' % (x + 1)
        elif winner == 'O':
            print 'Case #%d: O won' % (x + 1)
        elif winner == 'D':
            print 'Case #%d: Draw' % (x + 1)
        elif winner == 'U':
            print 'Case #%d: Game has not completed' % (x + 1)
        z = raw_input()
    return
                
if __name__ == "__main__":
    run()
    sys.exit(0)
            
