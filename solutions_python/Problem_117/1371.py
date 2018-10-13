import sys
import re



def checkrow(row, l, v):
    for i in range(l):
        if int(row[i]) > int(v):
            return False
    return True


def checkcol(rows, l, c, v):
    for i in range(l):
        if int(rows[i][c]) > int(v):
            return False
    return True


def checklawn(rows, n, m):
    for x in range(n):
        for y in range(m):
            if not checkrow(rows[x], m, rows[x][y]) and not checkcol(rows, n, y, rows[x][y]):
                return False
    return True

        
def main():
    f = open('B-large.in', 'r')
    output = open('B-large.out', 'w')
    text = f.read()
    f.close()
    lines = re.split("[\n|\r]",text)
    T = int(lines[0])
    i = 1
    
    for n in range(1,T+1):
        dims = lines[i].split(' ')
        i += 1
        N = int(dims[0])
        M = int(dims[1])
        rows = []
        for x in range(i,i+N):
            rows.append(lines[x].split(' '))
        i += N
        if N == 1:
            output.write('Case #' + str(n) + ': YES' +'\n')
        elif checklawn(rows, N, M):
            output.write('Case #' + str(n) + ': YES' +'\n')
        else:
            output.write('Case #' + str(n) + ': NO' +'\n')
            
    output.close()
    print 'done'
    

if __name__ == '__main__':
    main()
