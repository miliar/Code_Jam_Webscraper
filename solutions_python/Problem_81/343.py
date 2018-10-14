import sys

def read_case(infile):
    N = int(infile.readline())
    matrix = []

    for n in range(N):
        line = infile.readline().strip()
        row = []
        for c in line:
            if c == '0':
                row.append(0)
            elif c == '1':
                row.append(1)
            else:
                row.append(None)
        matrix.append(row)
    return matrix 
                

def solve_case(matrix):
    N = len(matrix)
    WP = [0] * N
    OWP = []
    OOWP = []
    wins = [0] * N
    games = [0] * N
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != None:
                wins[i] += matrix[i][j]
                games[i] += 1
        WP[i] = float(wins[i]) / float(games[i])
    for i in range(N):
        v = 0.0
        n = 0
        for j in range(N):
            if matrix[i][j] != None:
                n += 1
                v += float(wins[j] - matrix[j][i]) / (games[j] - 1)

        OWP.append(v / n)

    for i in range(N):
        n = 0
        avg = 0.0
        for j in range(N):
            if matrix[i][j] != None:
                avg += OWP[j]
                n += 1
        OOWP.append(float(avg) / float(n))
    result = [0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] for i in range(N)]
    return '\n' + '\n'.join(map(str, result))

if __name__ == '__main__':
    infile = sys.stdin
    T = int(infile.readline())      
    for i in range(T):
        case = read_case(infile)
        result = solve_case(case)
        print "Case #%d: %s" % (i + 1, result)
    
