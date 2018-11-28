import os
import sys
import math

def win(x, c):
    s = x.replace('T',c)
    if s == c+c+c+c:
        return True
    return False

def main(f):
    inFile = open(f)
    
    T = int(inFile.readline())

    r = []
    for i in xrange(0, T):
        v = [inFile.readline(), inFile.readline(), inFile.readline(), inFile.readline()]
        v = map(lambda x: x[:4], v)

        v += [v[0][0] + v[1][0] + v[2][0] + v[3][0]]
        v += [v[0][1] + v[1][1] + v[2][1] + v[3][1]]
        v += [v[0][2] + v[1][2] + v[2][2] + v[3][2]]
        v += [v[0][3] + v[1][3] + v[2][3] + v[3][3]]

        v += [v[0][0] + v[1][1] + v[2][2] + v[3][3]]
        v += [v[0][3] + v[1][2] + v[2][1] + v[3][0]]

        [is_x, is_o, is_not] = [False,False,False]
        for vv in v:
            is_x   = is_x or win(vv,'X')
            is_o   = is_o or win(vv,'O')
            is_not = is_not or ('.' in vv)

        if   is_x:   res = 'X won'
        elif is_o:   res = 'O won'
        elif is_not: res = 'Game has not completed'
        else:        res = 'Draw'

        inFile.readline()
        r.append(res)

    outFile = open(f.replace('.in', '.out'), 'w')
    for i in xrange(0, T):
        outFile.write('Case #%d: %s\n' % ((i+1), r[i]))
    outFile.close

if __name__ == '__main__':
    main('%s/%s' %(os.path.dirname(sys.argv[0]), 'A-large.in'))

