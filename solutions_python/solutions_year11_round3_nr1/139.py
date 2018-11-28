
inf = open('A-large.in', 'r')
outf = open('A-large.out', 'w')

T = int(inf.readline())
for case in range(1, T+1):
    (R,C) = inf.readline().rstrip().split(' ')
    m = []
    for i in range(0,int(R)):
        m.append(list(inf.readline().rstrip()))
    pos = False

    try:
        for i in range(0,int(R)):
            for j in range(0, int(C)):
                if m[i][j] == '#':
                    m[i][j] = '/'
                    
                    if m[i][j+1] == '.' or m[i+1][j] == '.' or m[i+1][j+1] == '.':
                        h=7/0
                    m[i][j+1] = '\\'
                    m[i+1][j] = '\\'
                    m[i+1][j+1] = '/'

        pos = True
    except:
        pos = False
    outf.write('Case #' + str(case) + ':\n')
    if pos:
        for i in range(0,int(R)):
            for j in range(0, int(C)):
                outf.write(m[i][j])
            outf.write('\n')
    else:
        outf.write('Impossible\n')
  #  print 'Case #' + str(case) + ': '

outf.close()
inf.close()
