import sys

def TicTac4(lines):
    Xsum = {'X': [0, 0, 0, 0], 'O': [0, 0, 0, 0]}
    Ysum = {'X': [0, 0, 0, 0], 'O': [0, 0, 0, 0]}
    diag1 = {'X': 0, 'O': 0}
    diag2 = {'X': 0, 'O': 0}
    total = 0

    for i in range(4):
        for j in range(4):
            ch = lines[i][j]
            if ch != '.':
                total = total + 1

            if i == j:
                if ch == 'X' or ch == 'O':
                    diag1[ch] = diag1[ch] + 1
                elif ch == 'T':
                    diag1['X'] = diag1['X'] + 1
                    diag1['O'] = diag1['O'] + 1

            if i + j == 3:
                if ch == 'X' or ch == 'O':
                    diag2[ch] = diag2[ch] + 1
                elif ch == 'T':
                    diag2['X'] = diag2['X'] + 1
                    diag2['O'] = diag2['O'] + 1

            if ch == 'X' or ch == 'O':
                Xsum[ch][j] = Xsum[ch][j] + 1
                Ysum[ch][i] = Ysum[ch][i] + 1

            if ch == 'T':
                Xsum['X'][j] = Xsum['X'][j] + 1
                Ysum['X'][i] = Ysum['X'][i] + 1
                Xsum['O'][j] = Xsum['O'][j] + 1
                Ysum['O'][i] = Ysum['O'][i] + 1

            if diag1['X'] >= 4 or diag2['X'] >= 4 or Xsum['X'][j] >= 4 or Ysum['X'][i] >= 4:
                return 'X won'
            if diag1['O'] >= 4 or diag2['O'] >= 4 or Xsum['O'][j] >= 4 or Ysum['O'][i] >= 4:
                return 'O won'

    #print "Start"
    #print lines
    #print Xsum
    #print Ysum
    #print diag1, diag2

    if total == 16:
        return 'Draw'
    return 'Game has not completed'
                

def runIt():
    input = sys.stdin
    n_tests = int(input.readline(), 10)
    
    for x in range(n_tests):
        lines = [input.readline() for i in range(4)]
        #print x, lines
        input.readline()
        #print TicTac4(lines)
        print ("Case #{0}: {1}".format(x+1, TicTac4(lines)))

runIt()

