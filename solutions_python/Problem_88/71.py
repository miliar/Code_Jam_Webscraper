import sys

def solve(f):
    R,C,D = map(int, f.readline().split())
    sheet = []
    sol = 'IMPOSSIBLE'
    for i in xrange(R):
        sheet.append(map(int,list(f.readline().strip())))
    d = min(R,C)
    while d >= 3:
        for j in xrange(C-d+1):
            for k in xrange(R-d+1):
                new_sheet = []
                for i in xrange(d):
                    new_sheet.append(sheet[i+k][j:j+d])
                L = len(new_sheet)
                new_sheet[0][0] = 0
                new_sheet[L-1][0] = 0
                new_sheet[0][L-1] = 0
                new_sheet[L-1][L-1] = 0
                center = (float(L-1)/2,float(L-1)/2)
                com = [0,0]
                for x in xrange(L):
                    for y in xrange(L):
                        com[0] += new_sheet[x][y]*(x-center[0])
                        com[1] += new_sheet[x][y]*(y-center[1])
                if com == [0.0,0.0]:
                    return d
        d -= 1
    return sol


def main(f):
    n = int(f.readline())
    for i in xrange(n):
        print 'Case #%d: %s' % (i+1,solve(f))

main(open(sys.argv[1],'r'))
