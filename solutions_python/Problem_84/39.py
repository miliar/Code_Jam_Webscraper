infile = open('A-large.in').readlines()
infile = [line.strip() for line in infile]
wfile = open('result', 'w')
T = int(infile[0])
infile = infile[1:]

for case_no in range(1, T+1):
    wfile.write('Case #%d:\n' %(case_no))
    R, C = [int(x) for x in infile[0].split()]
    infile = infile[1:]
    bw = infile[:R]
    infile = infile[R:]
    for i in range(R):
        bw[i] = list(bw[i])
        
    next_case = False
    for i in range(R):
        if next_case:
            break
        for j in range(C):
            if bw[i][j] == '#':
                if i == R-1 or j == C-1 or bw[i+1][j] != '#' or bw[i][j+1] != '#' or bw[i+1][j+1] != '#':
                    wfile.write('Impossible\n')
                    next_case = True
                    break
                bw[i][j] = '/'
                bw[i+1][j] = '\\'
                bw[i][j+1] = '\\'
                bw[i+1][j+1] = '/'
                
    if next_case:
        continue
    
    for line in bw:
        wfile.write(''.join(line) +'\n')
        
wfile.close()