#!/home/chenfzh/bin/python


def calc(rc):
    numrow = len(rc)
    numcol = len(rc[0])
    for i in range(0, numrow):
        for j in range(0, numcol):
            if rc[i][j] == '#':
                if i + 1 < numrow and j + 1 < numcol and\
                   rc[i][j+1]=='#'and rc[i+1][j]=='#'and rc[i+1][j+1]=='#':
                    rc[i][j] = '/'
                    rc[i][j+1] = '\\'
                    rc[i+1][j] = '\\'
                    rc[i+1][j+1] = '/'
                else:
                    return False
    return True                

def readfile(filename):
    f = open(filename)
    c = f.readlines()[1:]
    f.close();
    res = []
    tmp = []
    for i in c:
        if i[0] == '.' or i[0] == '#':
            line = [x for x in i]
            if line[-1] == '\n':
                line = line[:-1]
            tmp.append(line)
        elif len(tmp) > 0:
            res.append(tmp);
            tmp = []
    if len(tmp) > 0:
        res.append(tmp)
    return res


if __name__ == '__main__':
    import sys
    lines = readfile(sys.argv[1])
    for i in range(0, len(lines)):
        line = lines[i]
        print('Case #%d:' % (i + 1))
        if calc(line):
            for r in line:
                ss = ''
                for c in r:
                    ss += c
                print('%s' % ss)
        else:
            print('Impossible')

