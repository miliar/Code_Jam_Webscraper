'''
Created on Apr 13, 2013

@author: fniksic
'''
import sys

def test_cases():
    f = open(sys.argv[1])
    T = int(f.readline())
    for t in xrange(T):
        table = []
        for _ in xrange(4):
            table.append(f.readline().strip())
        f.readline()
        yield (t + 1, table)
        
def main():
    for (t, table) in test_cases():
        x, o = 0, 0
        end = True
        tom_i, tom_j = None, None
        row_x, row_o, col_x, col_o, diag_x, diag_o = [0] * 4, [0] * 4, [0] * 4, [0] * 4, [0] * 2, [0] * 2
        for i in xrange(4):
            for j in xrange(4):
                if table[i][j] == 'X':
                    x = x + 1
                    row_x[i] = row_x[i] + 1
                    col_x[j] = col_x[j] + 1
                    if i == j:
                        diag_x[0] = diag_x[0] + 1
                    if i == 3 - j:
                        diag_x[1] = diag_x[1] + 1
                elif table[i][j] == 'O':
                    o = o + 1
                    row_o[i] = row_o[i] + 1
                    col_o[j] = col_o[j] + 1
                    if i == j:
                        diag_o[0] = diag_o[0] + 1
                    if i == 3 - j:
                        diag_o[1] = diag_o[1] + 1
                elif table[i][j] == 'T':
                    tom_i = i
                    tom_j = j
                elif table[i][j] == '.':
                    end = False
        
        result = None
        if x > o: # X's move is last
            if tom_i != None:
                row_x[tom_i] = row_x[tom_i] + 1
                col_x[tom_j] = col_x[tom_j] + 1
                if tom_i == tom_j:
                    diag_x[0] = diag_x[0] + 1
                if tom_i == 3 - tom_j:
                    diag_x[1] = diag_x[1] + 1
            for i in xrange(4):
                if row_x[i] == 4 or col_x[i] == 4 or (i < 2 and diag_x[i] == 4):
                    result = "X won"
                    break
        else: # O's move is last
            if tom_i != None:
                row_o[tom_i] = row_o[tom_i] + 1
                col_o[tom_j] = col_o[tom_j] + 1
                if tom_i == tom_j:
                    diag_o[0] = diag_o[0] + 1
                if tom_i == 3 - tom_j:
                    diag_o[1] = diag_o[1] + 1
            for i in xrange(4):
                if row_o[i] == 4 or col_o[i] == 4 or (i < 2 and diag_o[i] == 4):
                    result = "O won"
                    break
        
        if result != None:
            print "Case #%d: %s" % (t, result)
        elif end:
            print "Case #%d: Draw" % t
        else:
            print "Case #%d: Game has not completed" % t
            
if __name__ == '__main__':
    main()