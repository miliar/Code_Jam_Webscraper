'''
Google Code Jam 

@author: khoipham
'''
def solve():
    global fin, fout
    fin = open('B-small.in', 'r')
    fout = open('B.out', 'w')
    
    cases = int(fin.readline())
    for caseIdx in range(1, cases + 1):
        line = fin.readline()
        [C, F, X] = s2af(line)
        
        maxFarms = int(X/(2*C) + 1000)
        d = [0.0 for _ in range(maxFarms)]
        for i in range(1, maxFarms):
            d[i] = d[i-1] + C/(F*(i-1) + 2) 
        
        result = X/2
        for i in range(1, maxFarms):
            tmp = d[i] + X/(F*i + 2)
            if tmp < result:
                result = tmp
        
        writeln('Case #%d: %.6f' % (caseIdx, result ))
        
    fin.close()
    fout.close()
    
def s2af(s, delimiter = ' '):
    return [float(i) for i in s.strip().split(delimiter)];

def s2ai(s, delimiter = ' '):
    return [int(i) for i in s.strip().split(delimiter)];
    
def array(initVal, cols, rows = 0):
    if rows == 0:
        return [initVal for _ in range(cols) ]
    return [[initVal for _ in range(cols)] for _ in range(rows) ]

# def write(s):
#    print(s, end='')
#    fout.write(s)

def writeln(s):
    print(s)
    fout.write(s + '\n')
        
fin = fout = None
if __name__ == '__main__':
    solve()
    