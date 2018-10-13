import re

def tic(f):
    with open(f,'r') as ifile:
        case  = int(ifile.readline())
        rlt = []
        pattern = re.compile('(XXXX|OOOO|XXXT|TXXX|OOOT|TOOO)')
        for i in range(case):
            flag = 1
            klist = []
            for j in range(4):
                tmp = ifile.readline()
                tmp = tmp.rstrip()
                klist.append(tmp)
            ifile.readline()
            diag1 = []
            diag2 = []
            for j in range(4):
                diag1.append(klist[j][j])
            for j in range(4):
                diag2.append(klist[j][3-j])
            klist.append(''.join(diag1))
            klist.append(''.join(diag2))
            for j in range(4):
                tmp = []
                for k in range(4):
                    tmp.append(klist[k][j])
                klist.append(''.join(tmp))
            for j in range(len(klist)):
                s = re.findall(pattern,klist[j])
                if len(s) > 0:
                    if s[0].count('X') > 0:
                        rlt.append('X won')
                    else:
                        rlt.append('O won')
                    flag = 0
                    break
            if flag == 1:
                cnt = 0
                for j in range(4):
                    cnt = cnt + klist[j].count('.')
                if cnt == 0:
                    rlt.append('Draw')
                else:
                    rlt.append('Game has not completed')
    with open('tic.txt', 'w') as wfile:
        for j in range(case):
            wfile.write('Case #{0}: {1}\n'.format(j+1,rlt[j]))
                
if __name__ == '__main__':
    import sys
    f = sys.argv[1]
    tic(f)
