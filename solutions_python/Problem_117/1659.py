import sys


def process_matrix(a):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            col_status = True
            for k in range(n):
                if( a[k][j] > a[i][j] ):
                    col_status = False
                    break
            row_status = True
            for k in range(m):
                if( a[i][k] > a[i][j] ):
                    row_status = False
                    break
            status = col_status or row_status
            if( not status ):
                return 'NO'
    return 'YES'


if (__name__ == '__main__'):
    num_cases = int(sys.stdin.readline())
    input = sys.stdin.readlines()
    i=0
    case = 1
    while(i < len(input)):
        row_num, col_num = map( int, input[i].split())
        a = []
        i+=1
        for j in range(row_num):
            a.append(input[i].split())
            i+=1
        print 'Case #%d:' % case, process_matrix(a)
        case+=1
