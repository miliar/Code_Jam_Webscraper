
import copy

class Log():
    def __init__(self, debug=False):
        self.debug = debug

    def info(self, fmt, *args):
        if self.debug:
            print fmt % args

def solve():
    NM = raw_input().split()
    N = int(NM[0])
    M = int(NM[1])
    
    mat = []
    for i in range(N):
        row = [e for e in raw_input().split()]
        mat.append(row)
            
    row = []
    col = []
    for i in range(N):
        row.append( {'min':10000, 'max':-1})

    for j in range(M):
        col.append({'min':10000, 'max':-1})    
    
    for i in range(N):
        for j in range(M):
            e = mat[i][j]
            if row[i]['min'] > e:
                row[i]['min'] = e
            if row[i]['max'] < e:
                row[i]['max'] = e
            
            if col[j]['min'] > e:
                col[j]['min'] = e
            if col[j]['max'] < e:
                col[j]['max'] = e
    for i in range(N):
        for j in range(M):
            e = mat[i][j]
            if row[i]['max'] > e and col[j]['max'] > e:
                return "NO"
    return  "YES"           
    
log = Log()
if __name__ == '__main__':
    case = int(raw_input())
    for i in range(1, case+1):
        ans = solve()
        print "Case #%d: %s"%(i, ans)