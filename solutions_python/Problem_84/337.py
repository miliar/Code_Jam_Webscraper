import sys

fin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

t = int(fin.readline())

for x in range(t):
    r, c = [int(x) for x in fin.readline().strip().split()]
    data = []
    for y in range(r):
        data.append(fin.readline().strip())
    data = [list(x) for x in data]

    impossible = False
    '''
    if r < 2 or c < 2:
        for a in range(r):
            for b in range(c):
                if data[a][b] == '#':
                    impossible = True
                    '''

    for a in range(r-1):
        for b in range(c-1):
            if data[a][b] == '#':
                if data[a+1][b] == '#' and\
                   data[a][b+1] == '#' and\
                   data[a+1][b+1] == '#':
                    data[a][b] = '/'
                    data[a+1][b] = '\\'
                    data[a][b+1] = '\\'
                    data[a+1][b+1] = '/'
                else:
                    impossible = True

    # check if any are left.
    
    for a in range(r):
        for b in range(c):
            if data[a][b] == '#':
                impossible = True
        
    if impossible:
        print('Case #' +str(x+1)+':\nImpossible')
    else:
        print('Case #' +str(x+1)+':')
        for n in data:
            print(''.join(n))
    
sys.stdout.close()
fin.close()
