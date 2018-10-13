'''
Google Code Jam 

@author: khoipham
'''
def s2ai(s, delimiter = ' '):
    return [int(i) for i in s.strip().split(delimiter)];
    
def array(initVal, cols, rows = 0):
    if rows == 0:
        return [initVal for _ in range(cols) ]
    return [[initVal for _ in range(cols)] for _ in range(rows) ]

def write(s):
    print(s, end='')
    fout.write(s)

def writeln(s):
    print(s)
    fout.write(s + '\n')

def solve(B):
    dp =  [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4) ]
    ci = [0, -1, -1, -1]
    cj = [-1, -1, 0, 1]
    tmp = False
    for i in range(4):
        for j in range(4):
            if B[i][j] == '.':
                tmp = True
            for k in range(4):
                ni = i + ci[k]
                nj = j + cj[k]
                if ni > -1 and nj > -1 and ni < 4 and nj < 4 and (B[i][j] == B[ni][nj] or B[i][j] == 'T'):
                    dp [i][j][k] = dp[ni][nj][k] + 1
                    
                    if dp[i][j][k] == 3 and B[i][j] != '.':
                        if B[i][j] != 'T' :
                            return B[i][j] + ' won'
                        else:
                            for k2 in range(4):
                                ni2 = i + ci[k2]
                                nj2 = j + cj[k2]  
                                if dp[ni2][nj2][k2] == 2:
                                    return B[ni2][nj2] + ' won'
    if tmp:
        return 'Game has not completed'
    return 'Draw'
    
fin = None
fout = None
if __name__ == '__main__':
    #fin = open('A.in', 'r')
    fin = open('A-small-attempt0.in', 'r')
    #fin = open('A-large.in', 'r')
    fout = open('A.out', 'w')
    
    cases = int(fin.readline())
    for caseIdx in range(1, cases + 1):
        B = array('.', 4, 4)
        for i in range(4):
            line = fin.readline()
            B[i] = [c for c in line.strip()]
        
        fin.readline()
        s = solve(B)
        writeln('Case #%d: ' % (caseIdx ) + s)
        
    fin.close()
    fout.close()
    