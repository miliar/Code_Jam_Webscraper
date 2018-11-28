import sys

WAIT_TOTAL = 0
WAIT_DIM = 1
WAIT_ROW = 2

def process_input():

    cases_count = 0

    rows = []
    rows_count = 0

    state = WAIT_TOTAL
    for line in sys.stdin.readlines():
        line = line.strip()
        if line != '':

            if state == WAIT_TOTAL:
                c = int(line)
                state = WAIT_DIM
            elif state == WAIT_DIM:
                (N,M) = map(lambda x: int(x), line.split(' '))
                state = WAIT_ROW
            elif state == WAIT_ROW:
                line = line.split(' ')
                line = map(lambda x: int(x), line)
                assert len(line) == M
                rows_count += 1
                rows.append(line)
                if rows_count == N:
                    cases_count += 1
                    assert cases_count <= c
                    ret = process_case(N,M,rows)
                    sys.stdout.write('Case #' + str(cases_count) + ': ')
                    print ret
                    rows = []
                    rows_count = 0
                    state = WAIT_DIM
            else:
                assert False

def process_case(N,M,pattern):

    #higger = max(max(pattern))
    #for i in range(higger,0,-1):
    #    print i

    for i in range(N):
        for j in range(M):
            #print 'ij:',i,j
            #print pattern[i][j]
            #nexts = next_to(i,j, N,M, pattern)

            a = None if j<=0 else pattern[i][j-1]
            b = None if i>=N-1 else pattern[i+1][j]
            c = None if j>=M-1 else pattern[i][j+1]
            d = None if i<=0 else pattern[i-1][j]
            act = pattern[i][j]

            row = pattern[i]
            column = [pattern[k][j] for k in range(0,N)]
            #print 'rc:',row,column

            if not valid_path(row, act) and not valid_path(column, act):
                return 'NO'
    return 'YES'

def valid_path(path,e):
    #print '1ret',path, '  e:',e
    ret = filter(lambda x: x>e, path)
    #print '2ret',ret
    return len(ret) == 0

def valid_path2(path):
    return path[0] == None or path[0] <= path[1] \
            and path[2] == None or path[2] <= path[1]

def le_next(nexts, x):
    nexts = filter(lambda y: y > x, nexts)
    return len(nexts) == 0

def next_to(i,j, N,M, pattern):
    ret = []
    if i > 0:
        ret.append( (i-1, j, pattern[i-1][j]) )
        if j > 0:
            pass
            #print '.'
            #ret.append(pattern[i-1][j-1])
        if j < M-1:
            #print '*'
            #ret.append(pattern[i-1][j+1])
            ret.append( (i, j+1, pattern[i][j+1]) )
    if i < N-1:
        ret.append( (i+1, j, pattern[i+1][j]) )
        if j > 0:
            pass
            #print 'o'
            #ret.append(pattern[i+1][j-1])
        if j < M-1:
            #print '_'
            #ret.append(pattern[i+1][j+1])
            ret.append( (i, j+1, pattern[i][j+1]) )
    print ret
    return ret

def border(i,j,N,M):
    return i == 0 or j == 0 or i == N-1 or j == M-1


if __name__ == '__main__':
    process_input()

